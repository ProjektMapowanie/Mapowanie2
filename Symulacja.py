import time
from threading import Thread
import serial

import serial
import struct


class Symulacja():
    def __init__(self):
        #self.ser = serial.Serial("COM5", 256000)
        t = Thread(target=self.func, args=())
        t2 = Thread(target=self.joinLandmark, args=())
        arduino_thread = Thread(target=self.readArduino, args=())

        arduino_thread.start()
        t.start()
        t2.start()

    def readArduino(self):

        while True:
            pass
            #vS = self.ser.read(48)
            #print(struct.unpack('ffffffffffff', vS))
            #self.sensor_list = struct.unpack('ffffffffffff', vS)



    def joinLandmark(self):
        for i in range(len(landmarksExample)):
            self.point = landmarksExample[i]
            time.sleep(0.1) #w sekundach

    def func(self):
        for i in range(len(trace)):
            self.coord = trace[i]
            time.sleep(0.03) #w sekundach



trace = [[350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 0], [350, 100, 2], [350, 100, 4], [350, 100, 6], [350, 100, 8], [350, 100, 10], [350, 100, 12], [350, 100, 14], [350, 100, 16], [350, 100, 18], [350, 100, 20], [350.7492131868318, 98.14563229086643, 22], [351.5626864729834, 96.31854137558123, 24], [352.43942876656155, 94.5209532829829, 26], [353.3783718921333, 92.75505809726505, 28], [354.3783718921333, 91.02300728969617, 30], [355.4382104205997, 89.32691109738332, 32], [356.5565962275412, 87.66883595227323, 34], [357.73216673212613, 86.05080196352333, 36], [358.96348968277744, 84.47478045630989, 38], [360.2490649021505, 82.94269157007193, 40], [361.58732611486823, 81.45640191911714, 42], [362.9766428557862, 80.01772231843984, 44], [364.4153224564635, 78.62840557752185, 46], [365.9016121074183, 77.29014436480414, 48], [367.43370099365626, 76.00456914543106, 50], [369.0097225008697, 74.77324619477974, 52], [370.6277564896196, 73.5976756901948, 54], [372.28583163472973, 72.47928988325332, 56], [373.98192782704257, 71.4194513547869, 58], [375.71397863461146, 70.4194513547869, 60], [377.4798738203293, 69.48050822921512, 62], [379.27746191292766, 68.60376593563696, 64], [381.1045528282129, 67.79029264948535, 66], [382.95892053734644, 67.04107946265353, 68], [384.83830577891825, 66.35703917600219, 70], [386.74041881150856, 65.73900518725229, 72], [388.6629422033852, 65.1877304756183, 74], [390.6035336559372, 64.70388668441896, 76], [392.5598288574048, 64.28806330278344, 78], [394.5294443634292, 63.94076694744958, 80], [396.5099805009123, 63.66242074552945, 82], [398.4990242916489, 63.45336381899415, 84], [400.49415239216853, 63.3138508715059, 86], [402.4929340462067, 63.2440518781009, 88], [404.4929340462067, 63.2440518781009, 90], [406.49171570024487, 63.3138508715059, 92], [408.4868438007645, 63.45336381899415, 94], [410.4758875915011, 63.66242074552945, 96], [412.4564237289842, 63.94076694744958, 98], [414.4260392350086, 64.28806330278344, 100], [416.3823344364762, 64.70388668441896, 102], [418.32292588902817, 65.1877304756183, 104], [420.24544928090484, 65.73900518725229, 106], [422.14756231349514, 66.35703917600219, 108], [424.02694755506695, 67.04107946265353, 110], [425.8813152642005, 67.79029264948535, 112], [427.70840617948573, 68.60376593563696, 114], [429.5059942720841, 69.48050822921512, 116], [431.27188945780193, 70.4194513547869, 118], [433.00394026537083, 71.4194513547869, 120], [434.70003645768367, 72.47928988325332, 122], [436.35811160279377, 73.5976756901948, 124], [437.9761455915437, 74.77324619477974, 126], [439.55216709875714, 76.00456914543106, 128], [441.0842559849951, 77.29014436480414, 130], [442.5705456359499, 78.62840557752185, 132], [444.0092252366272, 80.01772231843984, 134], [445.39854197754516, 81.45640191911714, 136], [446.7368031902629, 82.94269157007193, 138], [448.02237840963596, 84.47478045630989, 140], [449.25370136028727, 86.05080196352333, 142], [450.4292718648722, 87.66883595227323, 144], [451.5476576718137, 89.32691109738332, 146], [452.6074962002801, 91.02300728969617, 148], [453.6074962002801, 92.75505809726505, 150], [454.54643932585185, 94.5209532829829, 152], [455.42318161943, 96.31854137558123, 154], [456.2366549055816, 98.14563229086643, 156], [456.9858680924134, 100.0, 158], [457.66990837906474, 101.87938524157181, 160], [458.28794236781465, 103.78149827416212, 162], [458.83921707944864, 105.70402166603876, 164], [459.32306087064796, 107.64461311859075, 166], [459.73888425228347, 109.60090832005837, 168], [460.08618060761734, 111.57052382608278, 170], [460.3645268095375, 113.55105996356592, 172], [460.5735837360728, 115.54010375430246, 174], [460.71309668356105, 117.53523185482211, 176], [460.78289567696606, 119.53401350886031, 178], [460.78289567696606, 121.53401350886031, 180], [460.71309668356105, 123.53279516289851, 182], [460.5735837360728, 125.52792326341816, 184], [460.3645268095375, 127.5169670541547, 186], [460.08618060761734, 129.49750319163783, 188], [459.73888425228347, 131.46711869766224, 190], [459.32306087064796, 133.42341389912986, 192], [458.83921707944864, 135.36400535168184, 194], [458.28794236781465, 137.28652874355848, 196], [457.66990837906474, 139.18864177614878, 198], [456.9858680924134, 141.0680270177206, 200], [456.2366549055816, 142.92239472685418, 202], [455.42318161943, 144.74948564213938, 204], [454.54643932585185, 146.54707373473772, 206], [453.6074962002801, 148.31296892045557, 208], [452.6074962002801, 150.04501972802444, 210], [451.5476576718137, 151.7411159203373, 212], [450.4292718648722, 153.39919106544738, 214], [449.25370136028727, 155.01722505419727, 216], [448.02237840963596, 156.59324656141072, 218], [446.7368031902629, 158.12533544764867, 220], [445.39854197754516, 159.61162509860347, 222], [444.0092252366272, 161.05030469928076, 224], [442.5705456359499, 162.43962144019875, 226], [441.0842559849951, 163.77788265291647, 228], [439.55216709875714, 165.06345787228955, 230], [437.9761455915437, 166.29478082294085, 232], [436.35811160279377, 167.4703513275258, 234], [434.70003645768367, 168.5887371344673, 236], [433.00394026537083, 169.6485756629337, 238], [431.27188945780193, 170.6485756629337, 240], [429.5059942720841, 171.58751878850546, 242], [427.70840617948573, 172.46426108208362, 244], [425.8813152642005, 173.27773436823523, 246], [424.02694755506695, 174.02694755506707, 248], [422.14756231349514, 174.7109878417184, 250], [420.24544928090484, 175.3290218304683, 252], [418.32292588902817, 175.8802965421023, 254], [416.3823344364762, 176.36414033330163, 256], [414.4260392350086, 176.77996371493717, 258], [412.4564237289842, 177.12726007027103, 260], [410.4758875915011, 177.40560627219116, 262], [408.4868438007645, 177.61466319872648, 264], [406.5063076632814, 177.8930094006466, 262], [404.536692157257, 178.24030575598047, 260], [402.5803969557894, 178.656129137616, 258], [400.6398055032374, 179.13997292881535, 256], [398.71728211136076, 179.69124764044935, 254], [396.81516907877045, 180.30928162919923, 252], [394.93578383719864, 180.99332191585057, 250], [393.0814161280651, 181.7425351026824, 248], [391.25432521277986, 182.55600838883402, 246], [389.4567371201815, 183.43275068241218, 244], [387.69084193446366, 184.37169380798395, 242], [385.95879112689477, 185.37169380798395, 240], [384.26269493458193, 186.43153233645035, 238], [382.6046197894718, 187.54991814339184, 236], [380.9865858007219, 188.7254886479768, 234], [379.41056429350846, 189.9568115986281, 232], [377.8784754072705, 191.24238681800117, 230], [376.3921857563157, 192.5806480307189, 228], [374.9535061556384, 193.96996477163688, 226], [373.56418941472043, 195.40864437231417, 224], [372.2259282020027, 196.89493402326897, 222], [370.94035298262963, 198.42702290950692, 220], [369.70903003197833, 200.00304441672037, 218], [368.5334595273934, 201.62107840547026, 216], [367.4150737204519, 203.27915355058033, 214], [366.3552351919855, 204.9752497428932, 212], [365.3552351919855, 206.70730055046207, 210], [364.41629206641375, 208.47319573617992, 208], [363.5395497728356, 210.27078382877826, 206], [362.726076486684, 212.09787474406346, 204], [361.9768632998522, 213.95224245319704, 202], [361.29282301320086, 215.83162769476886, 200], [360.67478902445094, 217.73374072735916, 198], [360.12351431281695, 219.6562641192358, 196], [359.63967052161763, 221.59685557178778, 194], [359.2238471399821, 223.5531507732554, 192], [358.87655078464826, 225.5227662792798, 190], [358.5982045827281, 227.50330241676295, 188], [358.3891476561928, 229.4923462074995, 186], [358.24963470870455, 231.48747430801916, 184], [358.17983571529953, 233.48625596205736, 182], [358.17983571529953, 235.48625596205736, 180], [358.24963470870455, 237.48503761609555, 178], [358.3891476561928, 239.4801657166152, 176], [358.5982045827281, 241.46920950735176, 174], [358.87655078464826, 243.4497456448349, 172], [359.2238471399821, 245.41936115085932, 170], [359.63967052161763, 247.37565635232693, 168], [360.12351431281695, 249.3162478048789, 166], [360.67478902445094, 251.23877119675555, 164], [361.29282301320086, 253.14088422934586, 162], [361.9768632998522, 255.02026947091767, 160], [362.726076486684, 256.87463718005125, 158], [363.5395497728356, 258.7017280953365, 156], [364.41629206641375, 260.4993161879348, 154], [365.3552351919855, 262.2652113736527, 152], [366.3552351919855, 263.9972621812216, 150], [367.4150737204519, 265.6933583735344, 148], [368.4150737204519, 267.4254091811033, 150], [369.3540168460237, 269.19130436682116, 152], [370.23075913960184, 270.9888924594195, 154], [371.0442324257534, 272.81598337470473, 156], [371.79344561258523, 274.6703510838383, 158], [372.47748589923657, 276.5497363254101, 160], [373.0955198879865, 278.4518493580004, 162], [373.6467945996205, 280.374372749877, 164], [374.1306383908198, 282.314964202429, 166], [374.5464617724553, 284.2712594038966, 168], [374.89375812778917, 286.240874909921, 170], [375.1721043297093, 288.2214110474041, 172], [375.38116125624464, 290.21045483814066, 174], [375.5206742037329, 292.2055829386603, 176], [375.5904731971379, 294.2043645926985, 178], [375.5904731971379, 296.2043645926985, 180], [375.5206742037329, 298.20314624673665, 182], [375.38116125624464, 300.1982743472563, 184], [375.1721043297093, 302.18731813799286, 186], [374.89375812778917, 304.167854275476, 188], [374.5464617724553, 306.1374697815004, 190], [374.1306383908198, 308.09376498296797, 192], [373.6467945996205, 310.03435643551995, 194], [373.0955198879865, 311.9568798273966, 196], [372.47748589923657, 313.8589928599869, 198], [371.79344561258523, 315.73837810155874, 200], [371.0442324257534, 317.5927458106923, 202], [370.23075913960184, 319.4198367259775, 204], [369.3540168460237, 321.21742481857586, 206], [368.4150737204519, 322.9833200042937, 208], [367.4150737204519, 324.7153708118626, 210], [366.3552351919855, 326.41146700417545, 212], [365.236849385044, 328.06954214928555, 214], [364.0612788804591, 329.68757613803547, 216], [362.8299559298078, 331.2635976452489, 218], [361.5443807104347, 332.79568653148687, 220], [360.206119497717, 334.28197618244167, 222], [358.816802756799, 335.72065578311896, 224], [357.3781231561217, 337.10997252403695, 226], [355.8918335051669, 338.4482337367547, 228], [354.35974461892897, 339.73380895612775, 230], [352.7837231117155, 340.96513190677905, 232], [351.1656891229656, 342.140702411364, 234], [349.5076139778555, 343.25908821830546, 236], [347.81151778554266, 344.31892674677187, 238], [346.07946697797377, 345.31892674677187, 240], [344.3135717922559, 346.25786987234363, 242], [342.51598369965757, 347.1346121659218, 244], [340.68889278437234, 347.94808545207337, 246], [338.8345250752388, 348.6972986389052, 248], [336.955139833667, 349.3813389255565, 250], [335.05302680107667, 349.99937291430643, 252], [333.1305034092, 350.5506476259404, 254], [331.189911956648, 351.03449141713975, 256], [329.23361675518044, 351.45031479877525, 258], [327.264001249156, 351.7976111541091, 260], [325.2834651116729, 352.0759573560293, 262], [323.29442132093635, 352.2850142825646, 264], [321.2992932204167, 352.42452723005283, 266], [319.30051156637853, 352.49432622345785, 268], [317.30051156637853, 352.49432622345785, 270], [315.30172991234036, 352.42452723005283, 272], [313.3066018118207, 352.2850142825646, 274], [311.31755802108415, 352.0759573560293, 276], [309.33702188360104, 351.7976111541091, 278], [307.36740637757663, 351.45031479877525, 280], [305.411111176109, 351.03449141713975, 282], [303.470519723557, 350.5506476259404, 284], [301.5479963316804, 349.99937291430643, 286], [299.6458832990901, 349.3813389255565, 288], [297.7664980575183, 348.6972986389052, 290], [295.9121303483847, 347.94808545207337, 292], [294.0850394330995, 347.1346121659218, 294], [292.28745134050115, 346.25786987234363, 296], [290.5215561547833, 345.31892674677187, 298], [288.7895053472144, 344.31892674677187, 300], [287.09340915490156, 343.25908821830546, 302], [285.43533400979146, 342.140702411364, 304], [283.81730002104155, 340.96513190677905, 306], [282.2412785138281, 339.73380895612775, 308], [280.70918962759015, 338.4482337367547, 310], [279.22289997663535, 337.10997252403695, 312], [277.78422037595806, 335.72065578311896, 314], [276.39490363504007, 334.28197618244167, 316], [275.05664242232234, 332.79568653148687, 318], [273.77106720294927, 331.2635976452489, 320], [272.53974425229796, 329.68757613803547, 322], [271.36417374771304, 328.06954214928555, 324], [270.24578794077155, 326.41146700417545, 326], [269.18594941230515, 324.7153708118626, 328], [268.18594941230515, 322.9833200042937, 330], [267.2470062867334, 321.21742481857586, 332], [266.3702639931552, 319.4198367259775, 334], [265.55679070700364, 317.5927458106923, 336], [264.80757752017183, 315.73837810155874, 338], [264.1235372335205, 313.8589928599869, 340], [263.5055032447706, 311.9568798273966, 342], [262.9542285331366, 310.03435643552, 344], [262.47038474193727, 308.093764982968, 346], [262.05456136030176, 306.13746978150044, 348], [261.7072650049679, 304.16785427547603, 350], [261.42891880304774, 302.1873181379929, 352], [261.2198618765124, 300.19827434725636, 354], [261.0803489290242, 298.2031462467367, 356], [261.01054993561917, 296.20436459269854, 358], [261.01054993561917, 294.20436459269854, 360], [261.0803489290242, 292.20558293866037, 362], [261.2198618765124, 290.2104548381407, 364], [261.42891880304774, 288.22141104740416, 366], [261.70726500496784, 286.24087490992105, 368], [261.98561120688794, 284.26033877243793, 368], [262.26395740880804, 282.2798026349548, 368], [262.54230361072814, 280.2992664974717, 368], [262.82064981264824, 278.3187303599886, 368], [263.09899601456834, 276.3381942225055, 368], [263.37734221648844, 274.35765808502236, 368], [263.65568841840854, 272.37712194753925, 368], [263.86474534494386, 270.3880781568027, 366], [264.0042582924321, 268.39295005628304, 364], [264.0740572858371, 266.3941684022449, 362], [264.0740572858371, 264.3941684022449, 360], [264.0042582924321, 262.3953867482067, 358], [263.86474534494386, 260.40025864768705, 356], [263.65568841840854, 258.4112148569505, 354], [263.3773422164884, 256.4306787194674, 352], [263.0300458611545, 254.46106321344297, 350], [262.614222479519, 252.50476801197536, 348], [262.1303786883197, 250.56417655942337, 346], [261.5791039766857, 248.64165316754674, 344], [260.9610699879358, 246.73954013495643, 342], [260.27702970128445, 244.86015489338462, 340], [259.52781651445264, 243.00578718425103, 338], [258.71434322830106, 241.17869626896584, 336], [257.8376009347229, 239.3811081763675, 334], [256.89865780915113, 237.61521299064964, 332], [255.89865780915113, 235.88316218308077, 330], [254.83881928068473, 234.1870659907679, 328], [253.72043347374324, 232.52899084565783, 326], [252.5448629691583, 230.91095685690794, 324], [251.31354001850698, 229.3349353496945, 322], [250.0279647991339, 227.80284646345655, 320], [248.6897035864162, 226.31655681250174, 318], [247.3003868454982, 224.87787721182445, 316], [245.8617072448209, 223.48856047090646, 314], [244.3754175938661, 222.15029925818874, 312], [242.84332870762816, 220.86472403881567, 310], [241.2673072004147, 219.63340108816436, 308], [239.64927321166482, 218.4578305835794, 306], [237.99119806655474, 217.33944477663792, 304], [236.29510187424188, 216.27960624817152, 302], [234.563051066673, 215.27960624817152, 300], [232.79715588095516, 214.34066312259975, 298], [230.9995677883568, 213.4639208290216, 296], [229.17247687307162, 212.65044754286998, 294], [227.31810916393803, 211.90123435603817, 292], [225.43872392236622, 211.21719406938684, 290], [223.53661088977591, 210.59916008063695, 288], [221.61408749789928, 210.04788536900296, 286], [219.6734960453473, 209.5640415778036, 284], [217.71720084387968, 209.1482181961681, 282], [215.74758533785527, 208.80092184083423, 280], [213.76704920037213, 208.5225756389141, 278], [211.77800540963557, 208.3135187123788, 276], [209.78287730911592, 208.17400576489055, 274], [207.78409565507772, 208.10420677148554, 272], [205.78409565507772, 208.10420677148554, 270], [203.78531400103952, 208.17400576489055, 268], [201.79018590051987, 208.3135187123788, 266], [199.8011421097833, 208.5225756389141, 264], [197.82060597230017, 208.80092184083423, 262], [195.85099046627576, 209.1482181961681, 260], [193.89469526480815, 209.56404157780364, 258], [191.95410381225616, 210.04788536900298, 256], [190.03158042037953, 210.59916008063698, 254], [188.12946738778922, 211.21719406938686, 252], [186.2500821462174, 211.9012343560382, 250], [184.39571443708383, 212.65044754287004, 248], [182.56862352179863, 213.46392082902165, 246], [180.77103542920028, 214.3406631225998, 244], [179.00514024348243, 215.27960624817158, 242], [177.27308943591356, 216.27960624817158, 240], [175.5769932436007, 217.33944477663798, 238], [173.91891809849062, 218.45783058357947, 236], [172.30088410974074, 219.63340108816442, 234], [170.72486260252728, 220.86472403881572, 232], [169.19277371628934, 222.1502992581888, 230], [167.70648406533456, 223.48856047090652, 228], [166.26780446465727, 224.8778772118245, 226], [164.87848772373928, 226.3165568125018, 224], [163.54022651102156, 227.8028464634566, 222], [162.25465129164849, 229.33493534969455, 220], [161.02332834099718, 230.910956856908, 218], [159.84775783641223, 232.5289908456579, 216], [158.72937202947074, 234.18706599076796, 214], [157.66953350100434, 235.88316218308083, 212], [156.66953350100434, 237.6152129906497, 210], [155.73059037543257, 239.38110817636755, 208], [154.8538480818544, 241.1786962689659, 206], [154.0403747957028, 243.0057871842511, 204], [153.29116160887096, 244.86015489338467, 202], [152.60712132221963, 246.73954013495648, 200], [151.98908733346974, 248.6416531675468, 198], [151.43781262183575, 250.56417655942343, 196], [150.9539688306364, 252.50476801197541, 194], [150.5381454490009, 254.46106321344303, 192], [150.19084909366703, 256.43067871946744, 190], [149.9125028917469, 258.41121485695055, 188], [149.70344596521159, 260.4002586476871, 186], [149.56393301772334, 262.39538674820676, 184], [149.49413402431833, 264.39416840224493, 182], [149.49413402431833, 266.39416840224493, 180], [149.56393301772334, 268.3929500562831, 178], [149.70344596521159, 270.38807815680275, 176], [149.9125028917469, 272.3771219475393, 174], [150.19084909366703, 274.3576580850224, 172], [150.5381454490009, 276.32727359104683, 170], [150.9539688306364, 278.2835687925144, 168], [151.43781262183575, 280.2241602450664, 166], [151.98908733346974, 282.146683636943, 164], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162], [152.60712132221963, 284.0487966695333, 162]]


landmarksExample = [[300, 300], [300, 303], [300, 307], [302, 312], [300, 313], [301, 320], [300, 322], [300, 326],
             [300, 328], [300, 331], [301, 335], [300, 340], [300, 345],
             [200, 100], [205, 110], [211, 122], [217, 120], [221, 125], [224, 130], [225, 127],
             [224, 130], [225, 132], [231, 132], [237, 135], [238, 135], [244, 138], [245, 137],
             [246, 138], [246, 138], [242, 142], [227, 145], [245, 145], [251, 148], [252, 147],
              [253, 144], [255, 142], [256, 140], [257, 135], [260, 133], [260, 128], [263, 125],
              [265, 124], [270, 122], [273, 120], [277, 116], [277, 107], [279, 118], [280, 108],
      [500,400], [501,401], [504,403], [505,407], [518,411], [510,424], [512,417], [515,420],
      [516,423], [518,425], [521,428], [532,430]]
