#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os, fnmatch,wx
from wx.lib.mixins.listctrl import CheckListCtrlMixin
from stat import *
from optparse import OptionParser

#----------------------------
class HDDCleaner:
    def __init__(self,options):
        self.options=options
        self.patterns=options.patterns.split(",")
        self.maxSize=options.maxSize
        self.minSize=options.minSize
    
    def listDrives(self):
        if sys.platform == 'win32':
            try:
                import win32api
                drives=win32api.GetLogicalDriveStrings()
                drives=string.splitfields(drives,'\000')
                return drives
            except: # in case PyWin is not present we do it the classical way
                drives = []
                for i in range(ord('c'), ord('z')+1):
                    drive = chr(i)
                    if(os.path.exists(drive +":\\")):
                        drives.append(drive+":\\")
                return drives
               
    def listFilesByName(self, listOfFiles,directory,files):
        for fileName in files:
            for pattern in self.patterns:
                #print fnmatch.filter(fileName, pattern)
                if fnmatch.fnmatch(fileName, pattern):
                    filepath = os.path.join(directory,fileName)
                    if os.path.isfile(filepath):
                        filesize = os.stat(filepath)[ST_SIZE]
                        if filesize<=self.maxSize and filesize>=self.minSize:
                            listOfFiles[filepath] = filesize
                    break
   
    def scan(self,directories): 
        listOfFiles = {}
        for directory in directories: 
            sys.stdout.write('Scanning directory '+directory+'...\n')         
            directory = os.path.abspath(directory)
            os.path.walk(directory,self.listFilesByName,listOfFiles)       
        sys.stdout.write('Done scanning all dirs. Now sorting and building results.\n')
        allFiles = listOfFiles.items()
        allFiles.sort(self.list_compare)
        sortedList = allFiles
        return sortedList

    def list_compare(self,listX, listY):
        if listX[1]>listY[1]:
            return -1
        elif listX[1]==listY[1]:
            return 0
        else: # x<y
            return 1
#--------------------------------           
class CheckListCtrl(wx.ListCtrl, CheckListCtrlMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT)
        CheckListCtrlMixin.__init__(self)
        self.log = sys.stdout
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnItemActivated)

    def OnItemActivated(self, evt):
        self.ToggleItem(evt.m_itemIndex)
#--------------------------------
class FilesFrame(wx.Frame):     
    def __init__(self, parent, files): 
        wx.Frame.__init__( 
            self, parent, -1, "HDD Clean", size=(640,480) 
            ) 
        p = wx.Panel(self, -1, style=0) 
        b = wx.Button(p, -1, "Delete...") 
        b.SetDefault() 
        self.Bind(wx.EVT_BUTTON, self.OnDelete, b) 
        self.files=files
        self.list = CheckListCtrl(p)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(b, 0, wx.EXPAND)
        sizer.Add(self.list, 1, wx.EXPAND)
        p.SetSizer(sizer)
        
        self.list.InsertColumn(0, "Delete")
        self.list.InsertColumn(1, "Size",wx.LIST_FORMAT_RIGHT)
        self.list.InsertColumn(2, "File")
        self.list.InsertColumn(3, "Type")
        
        for i in self.files:
            index = self.list.InsertStringItem(sys.maxint,"")
            self.list.SetStringItem(index, 1, str(i[1]))
            self.list.SetStringItem(index, 2, str(i[0]))
            indexForFileType=str(i[0]).rfind(".")+1
            filetype="None"
            if indexForFileType!=0 and (len(str(i[0]))-indexForFileType<10):
                filetype=str(i[0])[indexForFileType:]
            self.list.SetStringItem(index, 3, filetype)
        
        self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(3, wx.LIST_AUTOSIZE)
        
        self.Show(1)

    def OnDelete(self, evt): 
        items=self.list.GetItemCount()
        allItems = range(0,items)
        allItems.reverse()
        for item in allItems:
            if self.list.IsChecked(item):
                listItem=self.list.GetItem(item,col=2)
                self.list.DeleteItem(item)
                os.remove(listItem.GetText())
#-------------------------------------------
def initOptions(parser):
    parser.add_option("-m", dest="minSize", default=-1,type="int", help="specify the minmial filesize to include in the list")
    parser.add_option("-M", dest="maxSize", default=99999999999999, type="int",help="specify the maximal filesize to include in the list")
    parser.add_option("-p", dest="patterns", default="*.*", help="commaseperated list of filetypes to filter for (e.g.: *.xml,*.fml)")
    parser.add_option("-f", dest="folder", default=None, help="specify which folder or drive to scan")
    parser.add_option("-n", dest="noGUI", action="store_false",default=True, help="do not show a GUI")
    parser.add_option("-o", dest="store", default="results.txt", help="if without GUI you may optionally specify a file to store the results in (result.txt=default)")
  
def main():
    parser=OptionParser()
    initOptions(parser)
    (options, args) = parser.parse_args()
    hd= HDDCleaner(options)
    myapp=wx.PySimpleApp()
    files={}
    foldercommand=options.folder
    patterns=options.patterns.split(",")
    if foldercommand!=None:
        folders=foldercommand.split(";")
        files=hd.scan(folders)
    else:
        allDrives = hd.listDrives()
        if allDrives==None:
            files = hd.scan("/")
        else:
            files= hd.scan(allDrives)
    if len(files)>0:
        if options.noGUI:
            FilesFrame(None,files)
            myapp.MainLoop()
        else:
            filename = options.store
            f=open(filename,'w')
            for file in files:
                entry=str(file[1])+"\t"+str(file[0])+"\n"
                f.write(entry)
            f.close()  
    else:
        print "No files found, exiting !"
    
if __name__=="__main__":
    main()
    
    
