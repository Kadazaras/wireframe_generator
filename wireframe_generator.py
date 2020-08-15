

#import System
import NXOpen
import NXOpen.UF
import NXOpen.UIStyler
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences
#import NXOpen.PointCollection

def getSelectedObject():
  returnSelectedObject = SelectAnObject("Please select an object")
  return returnSelectedObject

def SelectAnObject(prompt):
  theUI = NXOpen.UI.GetUI()
  #types = NXOpen.Selection.SelectFeatures()
  selector = theUI.SelectionManager
  selectedObjects = []
  objetos = ['Airfoil face','Root face']

  typeArray = [NXOpen.SelectionSelectionType.Faces]
  select_features = selector.SelectObjects('Select airfoil LE and TE faces','Select airfoil LE and TE faces',NXOpen.SelectionSelectionScope.WorkPart,False,typeArray)
  selectedObjects.append(select_features)
  typeArray = [NXOpen.SelectionSelectionType.Faces]
  select_features = selector.SelectObject('Select root lateral face','Select root lateral face',NXOpen.SelectionSelectionScope.WorkPart,False,typeArray)
  selectedObjects.append(select_features)
  typeArray = [NXOpen.SelectionSelectionType.Edges]
  select_features = selector.SelectObject('Select roof_tip edge','Select roof_tip edge',NXOpen.SelectionSelectionScope.WorkPart,False,typeArray)
  selectedObjects.append(select_features)
  return selectedObjects

def rotate_isocline(isocline):
  revolveBuilder1 = workPart.Features.CreateRevolveBuilder(NXOpen.Features.Feature.Null)
  revolveBuilder1.Limits.StartExtend.Value.RightHandSide = "0"
  revolveBuilder1.Limits.EndExtend.Value.RightHandSide = "360"
  revolveBuilder1.Limits.StartExtend.Value.RightHandSide = "-30"
  revolveBuilder1.Limits.EndExtend.Value.RightHandSide = "30"
  revolveBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
  targetBodies1 = [NXOpen.Body.Null] * 1
  targetBodies1[0] = NXOpen.Body.Null
  revolveBuilder1.BooleanOperation.SetTargetBodies(targetBodies1)
  revolveBuilder1.Offset.StartOffset.RightHandSide = "0"
  revolveBuilder1.Offset.EndOffset.RightHandSide = "5"
  revolveBuilder1.Tolerance = 0.01
  section1 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
  edgeDumbRule1 = workPart.ScRuleFactory.CreateRuleCurveFeature([isocline])
  rules1 = [None] * 1
  rules1[0] = edgeDumbRule1
  helpPoint1 = NXOpen.Point3d(0.0, 0.0, 0.0)
  section1.AllowSelfIntersection(False)
  section1.AddToSection(rules1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)
  revolveBuilder1.Section = section1
  revolveBuilder1.Limits.StartExtend.Value.RightHandSide = "-30"
  revolveBuilder1.Limits.EndExtend.Value.RightHandSide = "30"
  smartVolumeProfileBuilder1 = revolveBuilder1.SmartVolumeProfile
  smartVolumeProfileBuilder1.OpenProfileSmartVolumeOption = False
  smartVolumeProfileBuilder1.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
  starthelperpoint1 = [None] * 3
  starthelperpoint1[0] = 0.0
  starthelperpoint1[1] = 0.0
  starthelperpoint1[2] = 0.0
  revolveBuilder1.SetStartLimitHelperPoint(starthelperpoint1)
  endhelperpoint1 = [None] * 3
  endhelperpoint1[0] = 0.0
  endhelperpoint1[1] = 0.0
  endhelperpoint1[2] = 0.0
  revolveBuilder1.SetEndLimitHelperPoint(endhelperpoint1)
  revolveBuilder1.FeatureOptions.BodyType = NXOpen.GeometricUtilities.FeatureOptions.BodyStyle.Sheet
  datumAxis1 = workPart.Datums.FindObject("DATUM_CSYS(0) X axis")
  direction1 = workPart.Directions.CreateDirection(datumAxis1, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
  axis1 = workPart.Axes.CreateAxis(NXOpen.Point.Null, direction1, NXOpen.SmartObject.UpdateOption.WithinModeling)
  axis1.Point = NXOpen.Point.Null
  axis1.Evaluate()
  revolveBuilder1.Axis = axis1
  revolveBuilder1.ParentFeatureInternal = False
  feature1 = revolveBuilder1.CommitFeature()
  revolveBuilder1.Destroy()
  return feature1

def create_isocline(face):
  isoclineCurveBuilder1 = workPart.Features.FreeformCurveCollection.CreateIsoclineCurveBuilder(NXOpen.Features.IsoclineCurve.Null)
  boundaryFaces1 = []
  faceTangentRule1 = workPart.ScRuleFactory.CreateRuleFaceDumb(face)
  rules1 = [None] * 1
  rules1[0] = faceTangentRule1
  isoclineCurveBuilder1.Face.ReplaceRules(rules1, False)
  origin3 = NXOpen.Point3d(0.0, 0.0, 0.0)
  vector1 = NXOpen.Vector3d(0.0, 1.0, 0.0)
  direction1 = workPart.Directions.CreateDirection(origin3, vector1, NXOpen.SmartObject.UpdateOption.WithinModeling)

  isoclineCurveBuilder1.ReferenceDirection = direction1

  isoclineCurveBuilder1.CreateIsocline()
  airfoil_isocline = isoclineCurveBuilder1.Commit()
  isoclineCurveBuilder1.Destroy()
  return airfoil_isocline

def rotate_edge(edge):
  revolveBuilder1 = workPart.Features.CreateRevolveBuilder(NXOpen.Features.Feature.Null)
  revolveBuilder1.Limits.StartExtend.Value.RightHandSide = "0"
  revolveBuilder1.Limits.EndExtend.Value.RightHandSide = "360"
  revolveBuilder1.Limits.StartExtend.Value.RightHandSide = "-30"
  revolveBuilder1.Limits.EndExtend.Value.RightHandSide = "30"
  revolveBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
  targetBodies1 = [NXOpen.Body.Null] * 1
  targetBodies1[0] = NXOpen.Body.Null
  revolveBuilder1.BooleanOperation.SetTargetBodies(targetBodies1)
  revolveBuilder1.Offset.StartOffset.RightHandSide = "0"
  revolveBuilder1.Offset.EndOffset.RightHandSide = "5"
  revolveBuilder1.Tolerance = 0.01
  section1 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
  edgeDumbRule1 = workPart.ScRuleFactory.CreateRuleEdgeDumb(edge)
  rules1 = [None] * 1
  rules1[0] = edgeDumbRule1
  helpPoint1 = NXOpen.Point3d(0.0, 0.0, 0.0)
  section1.AllowSelfIntersection(False)
  section1.AddToSection(rules1, edge[0], NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)
  revolveBuilder1.Section = section1
  revolveBuilder1.Limits.StartExtend.Value.RightHandSide = "-30"
  revolveBuilder1.Limits.EndExtend.Value.RightHandSide = "30"
  smartVolumeProfileBuilder1 = revolveBuilder1.SmartVolumeProfile
  smartVolumeProfileBuilder1.OpenProfileSmartVolumeOption = False
  smartVolumeProfileBuilder1.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
  starthelperpoint1 = [None] * 3
  starthelperpoint1[0] = 0.0
  starthelperpoint1[1] = 0.0
  starthelperpoint1[2] = 0.0
  revolveBuilder1.SetStartLimitHelperPoint(starthelperpoint1)
  endhelperpoint1 = [None] * 3
  endhelperpoint1[0] = 0.0
  endhelperpoint1[1] = 0.0
  endhelperpoint1[2] = 0.0
  revolveBuilder1.FeatureOptions.BodyType = NXOpen.GeometricUtilities.FeatureOptions.BodyStyle.Sheet
  revolveBuilder1.SetEndLimitHelperPoint(endhelperpoint1)
  datumAxis1 = workPart.Datums.FindObject("DATUM_CSYS(0) X axis")
  direction1 = workPart.Directions.CreateDirection(datumAxis1, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
  axis1 = workPart.Axes.CreateAxis(NXOpen.Point.Null, direction1, NXOpen.SmartObject.UpdateOption.WithinModeling)
  axis1.Point = NXOpen.Point.Null
  axis1.Evaluate()
  revolveBuilder1.Axis = axis1
  revolveBuilder1.ParentFeatureInternal = False
  feature1 = revolveBuilder1.CommitFeature()
  revolveBuilder1.Destroy()
  return feature1

def intersect_revolved(revolved):
  intersectionCurveBuilder1 = workPart.Features.CreateIntersectionCurveBuilder(NXOpen.Features.Feature.Null)
  intersectionCurveBuilder1.CurveFitData.Tolerance = 0.01
  intersectionCurveBuilder1.CurveFitData.AngleTolerance = 0.5


  features1 = [NXOpen.Features.Feature.Null] * 1
  features1[0] = revolved
  faceFeatureRule1 = workPart.ScRuleFactory.CreateRuleFaceFeature(features1)

  rules1 = [None] * 1
  rules1[0] = faceFeatureRule1
  intersectionCurveBuilder1.FirstFace.ReplaceRules(rules1, False)

  added1 = intersectionCurveBuilder1.FirstSet.Add(revolved.GetFaces())

  faces1 = [NXOpen.DatumPlane.Null] * 1
  datumPlane1 = workPart.Datums.FindObject("DATUM_CSYS(0) XZ plane")
  faces1[0] = datumPlane1
  faceDumbRule1 = workPart.ScRuleFactory.CreateRuleFaceDatum(faces1)

  rules2 = [None] * 1
  rules2[0] = faceDumbRule1
  intersectionCurveBuilder1.SecondFace.ReplaceRules(rules2, False)

  objects2 = [NXOpen.TaggedObject.Null] * 1
  objects2[0] = datumPlane1
  added2 = intersectionCurveBuilder1.SecondSet.Add(objects2)
  nXObject1 = intersectionCurveBuilder1.Commit()
  intersectionCurveBuilder1.Destroy()

  return nXObject1

def create_line(points):
  associativeLineBuilder1 = workPart.BaseFeatures.CreateAssociativeLineBuilder(NXOpen.Features.AssociativeLine.Null)

  origin1 = NXOpen.Point3d(0.0, 0.0, 0.0)
  normal1 = NXOpen.Vector3d(0.0, 0.0, 1.0)
  plane1 = workPart.Planes.CreatePlane(origin1, normal1, NXOpen.SmartObject.UpdateOption.WithinModeling)
  unit1 = associativeLineBuilder1.Limits.StartLimit.Distance.Units
  expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
  expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
  associativeLineBuilder1.Limits.StartLimit.Distance.RightHandSide = "0"
  associativeLineBuilder1.StartPointOptions = NXOpen.Features.AssociativeLineBuilder.StartOption.Point
  associativeLineBuilder1.StartAngle.RightHandSide = "0"
  associativeLineBuilder1.EndPointOptions = NXOpen.Features.AssociativeLineBuilder.EndOption.Normal
  associativeLineBuilder1.EndAngle.RightHandSide = "90"
  associativeLineBuilder1.Limits.StartLimit.LimitOption = NXOpen.GeometricUtilities.CurveExtendData.LimitOptions.AtPoint
  associativeLineBuilder1.Limits.StartLimit.Distance.RightHandSide = "0"
  associativeLineBuilder1.Limits.EndLimit.LimitOption = NXOpen.GeometricUtilities.CurveExtendData.LimitOptions.Value
  associativeLineBuilder1.Limits.EndLimit.Distance.RightHandSide = "-50"
  associativeLineBuilder1.StartPointOptions = NXOpen.Features.AssociativeLineBuilder.StartOption.Inferred
  associativeLineBuilder1.EndPointOptions = NXOpen.Features.AssociativeLineBuilder.EndOption.Inferred
  associativeLineBuilder1.Limits.EndLimit.LimitOption = NXOpen.GeometricUtilities.CurveExtendData.LimitOptions.AtPoint
  associativeLineBuilder1.Limits.EndLimit.Distance.RightHandSide = "0"
  associativeLineBuilder1.StartPoint.Value = workPart.Points.CreatePoint(points[0])
  associativeLineBuilder1.StartPointOptions = NXOpen.Features.AssociativeLineBuilder.StartOption.Point
  expression4 = workPart.Expressions.CreateSystemExpression("100")
  scalar2 = workPart.Scalars.CreateScalarExpression(expression4, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
  associativeLineBuilder1.Limits.StartLimit.Distance.RightHandSide = "0"
  associativeLineBuilder1.Limits.EndLimit.Distance.RightHandSide = "62.7387398464592"
  associativeLineBuilder1.Limits.EndLimit.Distance.RightHandSide = "62.7387398464592"
  associativeLineBuilder1.EndPoint.Value = workPart.Points.CreatePoint(points[1])
  associativeLineBuilder1.EndPointOptions = NXOpen.Features.AssociativeLineBuilder.EndOption.Point
  nXObject1 = associativeLineBuilder1.Commit()
  associativeLineBuilder1.Destroy()
  return nXObject1





Session = NXOpen.Session.GetSession()
workPart = Session.Parts.Work
displayPart = Session.Parts.Display
lw = Session.ListingWindow


lw.Open()
mySelectedObject = getSelectedObject()
'these are the selections'
for i in mySelectedObject:
  pass
  #lw.WriteLine("Object: {}".format(str(i)))


#edges1 = mySelectedObject[0][1]
face1 = mySelectedObject[0][1] #Airfoil faces
face2 = mySelectedObject[1][1] #Root face
roof_tip_edge = mySelectedObject[2][1]

if type(roof_tip_edge) == NXOpen.Edge:
  roof_tip_point = roof_tip_edge.GetVertices()[0]
  height_roof_point = (roof_tip_point.Z**2+roof_tip_point.Y**2)**(1/2)
  roof_tip_3DPoint = NXOpen.Point3d(roof_tip_point.X,0.0,height_roof_point)
  roof_flag = 1
else:
  roof_flag = 0
 
#rotate_edge(edges1)

airfoil_isocline = create_isocline(face1) #Airfoil isoclines generated
isocline_rotated = rotate_isocline(airfoil_isocline) #Revolved sheet by revolving isoclines
root_face_rotated = rotate_edge(face2.GetEdges()) #Revolved root lateral face sheet body

a = intersect_revolved(isocline_rotated) # Intersection of isoclines at XZ
b = intersect_revolved(root_face_rotated) # Intersection of isoclines at XZ


start_end_points_airfoil = []
for i in a.GetEntities():
  if type(i) == NXOpen.Line or type(i) == NXOpen.Spline:
    if type(i) == NXOpen.Line:
      start_end_points_airfoil.append(i.EndPoint)
      start_end_points_airfoil.append(i.StartPoint)
      #lw.WriteLine("{}".format(str(type(i.EndPoint))))
      #lw.WriteLine("{}".format(str(type(i.StartPoint))))
    else:
      start_end_points_airfoil.append(i.Get3DPoles()[0])
      start_end_points_airfoil.append(i.Get3DPoles()[-1])

sorted_points_list = sorted(start_end_points_airfoil,key=lambda x: x.Z,reverse=True)
#for i in sorted_points_list:
  #lw.WriteLine('{}: {} {} {}'.format(type(i),i.X,i.Y,i.Z))

if roof_flag == 0:
  tip_line = create_line([sorted_points_list[0],sorted_points_list[1]])
if roof_flag == 1:
  tip_line1 = create_line([sorted_points_list[0],roof_tip_3DPoint])
  tip_line2 = create_line([roof_tip_3DPoint,sorted_points_list[1]])

'''displayModification1 = Session.DisplayManager.NewDisplayModification()
displayModification1.NewLayer = 90
displayModification1.Apply([airfoil_isocline,isocline_rotated,root_face_rotated])
displayModification1.Dispose()'''
workPart.Layers.MoveDisplayableObjects(90,root_face_rotated.GetBodies())
workPart.Layers.MoveDisplayableObjects(90,isocline_rotated.GetBodies())
workPart.Layers.MoveDisplayableObjects(90,airfoil_isocline.GetEntities())


existingReferenceSet_flag = 0
for i in workPart.GetAllReferenceSets():
  if i.Name == 'WIREFRAME':
    existingReferenceSet = i
    existingReferenceSet_flag = 1


if existingReferenceSet_flag == 0:
  referenceSet1 = workPart.CreateReferenceSet()
  referenceSet1.SetName("WIREFRAME")
  referenceSet1.SetAddComponentsAutomatically(True, True)
  if roof_flag == 0:
    referenceSet1.AddObjectsToReferenceSet(a.GetEntities())
    referenceSet1.AddObjectsToReferenceSet(b.GetEntities())
    referenceSet1.AddObjectsToReferenceSet(tip_line.GetEntities())
  if roof_flag == 1:
    referenceSet1.AddObjectsToReferenceSet(a.GetEntities())
    referenceSet1.AddObjectsToReferenceSet(b.GetEntities())
    referenceSet1.AddObjectsToReferenceSet(tip_line1.GetEntities())
    referenceSet1.AddObjectsToReferenceSet(tip_line2.GetEntities())
elif existingReferenceSet_flag == 1:
  if roof_flag == 0:
    existingReferenceSet.AddObjectsToReferenceSet(a.GetEntities())
    existingReferenceSet.AddObjectsToReferenceSet(b.GetEntities())
    existingReferenceSet.AddObjectsToReferenceSet(tip_line.GetEntities())
  if roof_flag == 1:
    existingReferenceSet.AddObjectsToReferenceSet(a.GetEntities())
    existingReferenceSet.AddObjectsToReferenceSet(b.GetEntities())
    existingReferenceSet.AddObjectsToReferenceSet(tip_line1.GetEntities())
    existingReferenceSet.AddObjectsToReferenceSet(tip_line2.GetEntities())



lw.Close()

