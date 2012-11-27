"""
File: graph.py
"""

class LinkedEdge(object):
    
    def __init__(self, fromVertex, toVertex, weight = None):         
        self._vertex1 = fromVertex
        self._vertex2 = toVertex
        self._weight = weight 
        self._mark = False
    
    def clearMark(self):
        self._mark = False
    
    def __eq__(self, other):
        if self is other: return True
        if type(self) != type(other):
            return False
        return self._vertex1 == other._vertex1 and \
               self._vertex2 == other._vertex2
    
    def getOtherVertex(self,  thisVertex):
        if thisVertex == None or thisVertex == self._vertex2:
            return self._vertex1
        else:
            return self._vertex2

    def getToVertex(self):
        return self._vertex2
    
    def getWeight(self):
        return self._weight
    
    def isMarked(self): 
        return self._mark
    
    def setMark(self):
        self._mark = True
    
    def setWeight(self, weight):
        self._weight = weight     
          
    def __str__(self):
        return str(self._vertex1) + ">" + \
               str(self._vertex2)   + ":" + \
               str(self._weight)

class LinkedVertex(object):

    def __init__(self, label):
        self._label = label
        self._edgeList = []
        self._mark = False

    def clearMark(self):
        self._mark = False;
    
    def getLabel(self): 
        return self._label
    
    def isMarked(self): 
        return self._mark
    
    def setLabel(self, label, g):
        g._vertices.pop(self._label, None)
        g._vertices[label] = self
        self._label = label          

    def setMark(self):
        self._mark = True
    
    def __str__(self):
        return str(self._label)

    # Methods used by LinkedGraph
    
    def addEdgeTo(self, toVertex, weight):
        edge = LinkedEdge(self, toVertex, weight)
        self._edgeList.append(edge)
    
    def getEdgeTo(self, toVertex):
        edge = LinkedEdge(self, toVertex)
        try:
            return self._edgeList[self._edgeList.index(edge)]
        except:
            return None

    def incidentEdges(self):
        return iter(self._edgeList)
        
    def neighboringVertices(self):
        vertices = []
        for edge in self._edgeList:
            vertices.append(edge.getOtherVertex(self))
        return iter(vertices)
            
    def removeEdgeTo(self, toVertex):
        edge = LinkedEdge(self, toVertex)
        if edge in self._edgeList:
            self._edgeList.remove(edge)
            return True
        else:
            return False


class LinkedDirectedGraph(object):

    def __init__(self, collection = None):
        self._vertexCount = 0
        self._edgeCount = 0
        self._vertices = {}
        if collection != None:
            for label in collection:
                self.addVertex(label)
                
    # Methods for clearing, marks, sizes, string rep

    def clear(self):
        self._vertexCount = 0
        self._edgeCount = 0
        self._vertices = {}        

    def clearEdgeMarks(self):
        for edge in self.edges():
            edge.clearMark()
    
    def clearVertexMarks(self):
        for vertex in self.vertices():
            vertex.clearMark()
    
    def isEmpty(self):
        return self._vertexCount == 0;

    def sizeEdges(self):
        return self._edgeCount
    
    def sizeVertices(self):
        return self._vertexCount
    
    def __str__(self):
        result = str(self.sizeVertices()) + " Vertices: "
        for vertex in self._vertices:
            result += " " + str(vertex)
        result += "\n";
        result += str(self.sizeEdges()) + " Edges: "
        for edge in self.edges():
            result += " " + str(edge)
        return result

    # Vertex related methods
    
    def addVertex(self, label):
        self._vertices[label] = LinkedVertex(label)
        self._vertexCount += 1
        
    def containsVertex (self, label):
        return label in self._vertices
    
    def getVertex(self, label):
        return self._vertices[label]
    
    def removeVertex(self,  label):
        removedVertex = self._vertices.pop(label, None)
        if removedVertex is None: 
            return False
        
        # Examine all vertices
        for vertex in self.vertices():
            if vertex.removeEdgeTo(removedVertex): 
                self._edgeCount -= 1
        self._vertexCount -= 1
        return True
    
    # Methods related to edges

    def addEdge(self, fromLabel, toLabel, weight):
        fromVertex = self.getVertex(fromLabel)
        toVertex   = self.getVertex(toLabel)
        fromVertex.addEdgeTo(toVertex, weight)
        self._edgeCount += 1
    
    def containsEdge(self, fromLabel, toLabel):
        return self.getEdge(fromLabel, toLabel) != None
    
    def getEdge(self, fromLabel, toLabel):
        fromVertex = self._vertices[fromLabel]
        toVertex   = self._vertices[toLabel]
        return fromVertex.getEdgeTo(toVertex)
    
    def removeEdge (self, fromLabel, toLabel): 
        fromVertex = self.getVertex(fromLabel)     
        toVertex   = self.getVertex(toLabel)     
        edgeRemovedFlg = fromVertex.removeEdgeTo(toVertex)
        if edgeRemovedFlg: 
            self._edgeCount -= 1
        return edgeRemovedFlg

    # Iterators
    
    def edges(self):
        result = set()
        for vertex in self.vertices():
            edges = vertex.incidentEdges()
            result = result.union(set(edges))
        return iter(result)
    
    def vertices(self):
        return iter(self._vertices.values())

    def incidentEdges(self, label):
        return self._vertices[label].incidentEdges()
    
    def neighboringVertices(self, label):
        return self._vertices[label].neighboringVertices()
    
