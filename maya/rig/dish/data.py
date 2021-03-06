import maya.cmds as mc
def excludeParentAttribute ():
    nodeType = ['controlPoint','geometryShape','containerBase' ]
    unExposeAttr = []
    for nde in nodeType:
        attrList = mc.attributeInfo( inherited=False, t=nde  )

        if attrList is not None:
            unExposeAttr.extend(attrList)
    return unExposeAttr

face            = ['ear','lid','brow','nose','eye','mouth','lip','chin','forehead']
limbs           = ['arm','foot','hand ','leg','foot','toe','spine','head','neck']
articulations   = ['shoulder','elbow','wrist','finger','thigh','knee','ankle']
groupType       = ['SYS','GRP','ZERO','OFFSET','HOOK','ANCHOR','Pivot','CTRLS','Space','Input','Output','Drivers']
clothParts      = [ 'sleeve','stitch','skirt','coat','shirt','pants','collar','dress']

recipeData = {'author':'cedricbazillou@gmail.com','gitSource':'https://github.com/cedricB/circeCharacterWorksTools'}

surfceExclude =[u'curvePrecision', u'uDivisionsFactor', u'minValueU', u'minValueV',
 u'useChordHeightRatio', u'degreeV', u'degreeU', u'simplifyV', u'objSpaceChordHeight', u'formU',
 u'simplifyU', u'displayRenderTessellation', u'dispSF', u'vDivisionsFactor', u'chordHeight',
 u'degreeUV', u'tweakSizeU', u'chordHeightRatio', u'spansV', u'create', u'minMaxRangeV',
 u'minMaxRangeU', u'numberV', u'numberU', u'trimFace', u'patchUVIds', u'curvatureTolerance',
 u'selCVDisp', u'modeV', u'modeU', u'tweakSizeV', u'dispOrigin', u'smoothEdgeRatio',
 u'useChordHeight', u'normalsDisplayScale', u'edgeSwap', u'maxValueV', u'maxValueU',
 u'spansUV', u'renderTriangleCount', u'explicitTessellationAttributes', u'simplifyMode',
 u'curvePrecisionShaded', u'divisionsV', u'divisionsU', u'smoothEdge', u'basicTessellationType',
 u'fixTextureWarp', u'gridDivisionPerSpanV', u'gridDivisionPerSpanU', u'spansU', u'formV']

crveExclude = [u'degree', u'visibility',
 u'intermediateObject',
 u'spans', u'dispEP',
 u'minValue',
 u'compInstObjGroups.compObjectGroups.compObjectGrpCompList',
 u'header',
 u'worldNormal',
 u'minMaxValue',
 u'controlPoints.xValue',
 u'colorSet.colorSetPoints.colorSetPointsG',
 u'dispCurveEndPoints',
 u'colorSet.colorSetPoints.colorSetPointsB',
 u'colorSet.colorSetPoints.colorSetPointsA',
 u'dispGeometry',
 u'worldMatrix', u'template', u'compInstObjGroups.compObjectGroups',
 u'colorSet.colorSetPoints.colorSetPointsR',
 u'controlPoints.yValue', u'tweakSize', u'uvSet.uvSetPoints',
 u'uvSet.uvSetPoints.uvSetPointsV',
 u'uvSet.uvSetPoints.uvSetPointsU',
 u'worldNormal.worldNormalZ',
 u'inPlace', u'worldNormal.worldNormalX', u'colorSet.clamped',
 u'colorSet.colorSetPoints', u'controlPoints.zValue',
 u'compInstObjGroups.compObjectGroups.compObjectGroupId',
 u'worldNormal.worldNormalY', u'maxValue', u'uvSet.uvSetName',
 u'editPoints.xValueEp', u'colorSet.colorName', u'editPoints.zValueEp',
 u'uvSet.uvSetTweakLocation', u'form', u'editPoints.yValueEp', 
 u'colorSet.representation', u'dispCV',u'localScaleX', 
 u'localScale', u'localPosition', u'underWorldObject', u'localPositionZ', u'localScaleZ', u'localPositionX', u'localPositionY', u'worldPosition.worldPositionZ', u'localScaleY', u'worldPosition.worldPositionX', u'worldPosition.worldPositionY' ]

latExclude   = [u'origin', u'sDivisions', u'latticePointMoved',   u'dispLattice', u'dispPoints',
 u'originY', u'originX', u'originZ' , u'uDivisions',  u'tDivisions', u'displayControl']

meshExclude  = [u'displayAlphaAsGreyScale', u'holeFaceData', u'displayEdges', u'numTriangles',
 u'vertexColor.vertexAlpha', u'backfaceCulling', u'colors', u'initialSampleRate', u'doubleSided',
 u'creaseVertexData', u'smoothLevel', u'useMinEdgeLength', u'vertexNormal', u'renderSmoothLevel',
 u'collisionOffsetVelocityMultiplier.collisionOffsetVelocityMultiplier_FloatValue', u'featureDisplacement',
 u'collisionDepthVelocityIncrement', u'vertexNormal.vertexNormalX', u'vertexNormal.vertexNormalY', u'uvSize',
 u'vertexColor.vertexFaceColor.vertexFaceColorB', u'boundaryRule', u'userTrg', u'continuity', u'vrts.vrtz',
 u'vrts.vrtx', u'vrts.vrty', u'parentMatrix', u'displayTangent', u'vertexBackfaceCulling', 
 u'vertexColor.vertexFaceColor.vertexFaceColorG', u'displayTriangles', u'collisionDepthVelocityMultiplier',
 u'boundingBoxScaleY', u'normalPerVertex', u'vertexNormal.vertexFaceNormal.vertexFaceNormalZ', u'sofy', u'sofz',
 u'vertexNormal.vertexFaceNormal.vertexFaceNormalY', u'collisionDepthVelocityIncrement.collisionDepthVelocityIncrement_Interp',
 u'perInstanceTag', u'normalSize', u'colors.colorG', u'collisionOffsetVelocityMultiplier.collisionOffsetVelocityMultiplier_Position',
 u'colors.colorA', u'colors.colorB', u'outForceNodeUVUpdate', u'uvpt', u'keepMapBorders', u'useMaxEdgeLength', 
 u'displayFacesWithGroupId', u'maxSubd', u'sofx', u'boundingBoxScaleX', 
 u'boundingBoxScaleZ', u'displayItemNumbers', u'vertexNormal.vertexFaceNormal.vertexFaceNormalX',
 u'vertexColor.vertexColorG', u'vertexColor.vertexColorB', u'smoothShading', u'vertexColor.vertexFaceColor',
 u'dispResolution', u'borderWidth', u'parentInverseMatrix', u'maxTriangles', u'keepBorder',
 u'collisionOffsetVelocityIncrement.collisionOffsetVelocityIncrement_Interp', u'quadSplit', u'maxEdgeLength',
 u'uvTweakLocation', u'allowTopologyMod', u'collisionOffsetVelocityIncrement.collisionOffsetVelocityIncrement_FloatValue',
 u'displaySubdComps', u'vertexIdMap', u'vertexNormal.vertexFaceNormal', u'tangentSmoothingAngle',
 u'collisionOffsetVelocityIncrement.collisionOffsetVelocityIncrement_Position',
 u'materialBlend', u'maxUv', u'pnts', u'boundingBoxScale', u'collisionOffsetVelocityMultiplier',
 u'normalType', u'collisionDepthVelocityIncrement.collisionDepthVelocityIncrement_FloatValue', u'faceIdMap', 
 u'lodVisibility', u'extraSampleRate', u'collisionDepthVelocityIncrement.collisionDepthVelocityIncrement_Position', 
 u'minScreen', u'cachedSmoothMesh', u'pnts.pntz', u'useNumTriangles', u'pnts.pntx', u'pnts.pnty',
 u'vertexNormal.vertexNormalZ', u'vertexNormalMethod', u'vrts', u'smoothUVs', u'displayVertices',
 u'vertexColor.vertexColorRGB', u'creaseData', u'inForceNodeUVUpdate', u'keepHardEdge', 
 u'cachedInMesh', u'displayCenter', u'tangentNormalThreshold', u'displaySmoothMesh',
 u'outGeometryClean', u'vertexColor.vertexFaceColor.vertexFaceColorRGB', u'displayInvisibleFaces',
 u'collisionDepthVelocityMultiplier.collisionDepthVelocityMultiplier_Interp', u'vertexNormal.vertexNormalXYZ',
 u'collisionOffsetVelocityIncrement', u'propagateEdgeHardness',
 u'collisionDepthVelocityMultiplier.collisionDepthVelocityMultiplier_FloatValue', u'motionVectorColorSet',
 u'perInstanceIndex', u'colors.colorR', u'useMinScreen', 
 u'collisionOffsetVelocityMultiplier.collisionOffsetVelocityMultiplier_Interp', u'edgeIdMap', u'vertexColor',
 u'outSmoothMesh', u'worldInverseMatrix', u'face', u'collisionDepthVelocityMultiplier.collisionDepthVelocityMultiplier_Position', 
 u'smoothMeshSelectionMode', u'uvpt.uvpy', u'uvpt.uvpx', u'vertexColor.vertexFaceColor.vertexFaceAlpha', 
 u'useMaxSubdivisions', u'displayNormal', u'reuseTriangles', u'vertexSize', u'edge.edgh', 
 u'minEdgeLength', u'vertexNormal.vertexFaceNormal.vertexFaceNormalXYZ', u'nodeState', u'opposite',
 u'displayUVs', u'normalThreshold', u'smoothWarn', u'colorPerVertex', 
 u'vertexColor.vertexColorR', u'vertexColor.vertexFaceColor.vertexFaceColorR', u'normals.normalz',
 u'normals.normalx', u'normals.normaly', u'useMaxUV', u'edge.edg1', u'edge.edg2', u'displayNonPlanar',
 u'displayHWEnvironment', u'tangentSpace', u'displayBorders', u'textureThreshold', u'edge', 
 u'normals', u'inverseMatrix', u'smoothOffset', u'ignoreHwShader', u'useSmoothPreviewForRender',  u'matrix']

defaultNodes = [u'time1', u'sequenceManager1', u'renderPartition',
        u'renderGlobalsList1', u'defaultLightList1', u'defaultShaderList1',
        u'postProcessList1', u'defaultRenderUtilityList1',
        u'defaultRenderingList1', u'lightList1',
        u'defaultTextureList1', u'lambert1', u'particleCloud1',
        u'initialShadingGroup', u'initialParticleSE', u'initialMaterialInfo',
        u'shaderGlow1', u'dof1', u'defaultRenderGlobals', 
        u'defaultRenderQuality', u'defaultResolution', u'defaultLightSet',
        u'defaultObjectSet', u'defaultViewColorManager', u'hardwareRenderGlobals',
        u'hardwareRenderingGlobals', u'characterPartition', u'defaultHardwareRenderGlobals',
        u'ikSystem', u'hyperGraphInfo', u'hyperGraphLayout', u'globalCacheControl', 
        u'dynController1', u'strokeGlobals', u'CustomGPUCacheFilter', u'objectTypeFilter74',
        u'persp', u'perspShape', u'top', u'topShape', u'front', u'frontShape', u'side', u'sideShape',
        u'lightLinker1', u'layersFilter', u'objectTypeFilter75', u'animLayersFilter',
        u'objectTypeFilter76', u'notAnimLayersFilter', u'objectTypeFilter77',
        u'defaultRenderLayerFilter', u'objectNameFilter4', u'renderLayerFilter',
        u'objectTypeFilter78', u'objectScriptFilter10', u'renderingSetsFilter',
        u'objectTypeFilter79', u'relationshipPanel1LeftAttrFilter', u'relationshipPanel1RightAttrFilter',
        u'layerManager', u'defaultLayer', u'renderLayerManager', u'defaultRenderLayer']
        
excludeAttr = ['message', 'caching ','isHistoricallyInteresting',
        'binMembership','hyperLayout', 'isCollapsed', 'blackBox',
        'borderConnections','isHierarchicalConnection','publishedNodeInfo',
        'publishedNodeInfo.publishedNode','publishedNodeInfo.isHierarchicalNode',
        'publishedNodeInfo.publishedNodeType','rmbCommand',
        'templateName','templatePath','viewName','iconName','viewMode',
        'templateVersion','uiTreatment','customTreatment',
        'creator','creationDate','containerType',
        'boundingBox','boundingBoxMin','boundingBoxMinX','boundingBoxMinY','boundingBoxMinZ','boundingBoxMax',
        'boundingBoxMaxX','boundingBoxMaxY','boundingBoxMaxZ','boundingBoxSize','boundingBoxSizeX',
        'boundingBoxSizeY','boundingBoxSizeZ','center','boundingBoxCenterX','boundingBoxCenterY',
        'boundingBoxCenterZ','ghosting','instObjGroups',
        'instObjGroups.objectGroups','instObjGroups.objectGroups.objectGrpCompList',
        'instObjGroups.objectGroups.objectGroupId','instObjGroups.objectGroups.objectGrpColor',
        'useObjectColor','objectColor','drawOverride','overrideDisplayType',
        'overrideLevelOfDetail','overrideShading','overrideTexturing',
        'overridePlayback','overrideEnabled','overrideVisibility',
        'overrideColor', 'renderInfo','identification','layerRenderable','layerOverrideColor',
        'renderLayerInfo','renderLayerInfo.renderLayerId','renderLayerInfo.renderLayerRenderable',
        'renderLayerInfo.renderLayerColor','ghostingControl','ghostCustomSteps',
        'ghostPreSteps','ghostPostSteps','ghostStepSize','ghostFrames','ghostColorPreA',
        'ghostColorPre','ghostColorPreR','ghostColorPreG','ghostColorPreB', 
        'ghostColorPostA','ghostColorPost','ghostColorPostR','ghostColorPostG',
        'ghostColorPostB','ghostRangeStart','ghostRangeEnd','ghostDriver',
        'shear','shearXY','shearXZ','shearYZ','rotatePivot','rotatePivotX',
        'rotatePivotY','rotatePivotZ','rotatePivotTranslate','rotatePivotTranslateX',
        'rotatePivotTranslateY','rotatePivotTranslateZ','scalePivot','scalePivotX',
        'scalePivotY','scalePivotZ','scalePivotTranslate','scalePivotTranslateX','scalePivotTranslateY', 
        'scalePivotTranslateZ','rotateAxis','rotateAxisX','rotateAxisY','rotateAxisZ','transMinusRotatePivot',
        'transMinusRotatePivotX','transMinusRotatePivotY','transMinusRotatePivotZ','minTransLimit','minTransXLimit',
        'minTransYLimit','minTransZLimit','maxTransLimit','maxTransXLimit','maxTransYLimit','maxTransZLimit','minTransLimitEnable',
        'minTransXLimitEnable','minTransYLimitEnable','minTransZLimitEnable','maxTransLimitEnable','maxTransXLimitEnable',
        'maxTransYLimitEnable','maxTransZLimitEnable','minRotLimit','minRotXLimit','minRotYLimit','minRotZLimit','maxRotLimit',
        'maxRotXLimit','maxRotYLimit','maxRotZLimit','minRotLimitEnable','minRotXLimitEnable','minRotYLimitEnable','minRotZLimitEnable',
        'maxRotLimitEnable','maxRotXLimitEnable','maxRotYLimitEnable','maxRotZLimitEnable','minScaleLimit','minScaleXLimit','minScaleYLimit',
        'minScaleZLimit','maxScaleLimit','maxScaleXLimit','maxScaleYLimit','maxScaleZLimit','minScaleLimitEnable','minScaleXLimitEnable',
        'minScaleYLimitEnable','minScaleZLimitEnable','maxScaleLimitEnable','maxScaleXLimitEnable','maxScaleYLimitEnable',
        'maxScaleZLimitEnable','geometry','xformMatrix', 'selectHandle', 'selectHandleX', 'selectHandleY', 'selectHandleZ', 
        'displayHandle','displayScalePivot','displayRotatePivot','displayLocalAxis','dynamics',
        'showManipDefault','specifiedManipLocation','rotateQuaternion','rotateQuaternionX','rotateQuaternionY','rotateQuaternionZ', 
        'rotateQuaternionW','rotationInterpolation','element','foodType','uuID','cached','caching','moduleInfos',
        u'editPoints',  u'dispHull']

unExposeAttr = excludeParentAttribute ()

    
