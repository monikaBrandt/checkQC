
import os

import unittest

import pandas as pd
import numpy as np

from interop import imaging

from checkQC.parsers.interop_parser import InteropParser


class TestInteropParser(unittest.TestCase):

    class Receiver(object):
        def __init__(self):
            self.error_rate_values = []
            self.percent_q30_values = []
            self.percent_q30_per_cycle = []
            self.subscriber = self.subscribe()
            next(self.subscriber)

        def subscribe(self):
            while True:
                interop_stat = yield
                key = list(interop_stat)[0]
                if key == "error_rate":
                    self.error_rate_values.append(interop_stat)
                if key == "percent_q30":
                    self.percent_q30_values.append(interop_stat)
                if key == "percent_q30_per_cycle":
                    self.percent_q30_per_cycle.append(interop_stat)

        def send(self, value):
            self.subscriber.send(value)

    runfolder = os.path.join(os.path.dirname(__file__), "..", 
                             "resources",
                             "MiSeqDemo")
    interop_parser = InteropParser(runfolder=runfolder, 
                                   parser_configurations=None)
    subscriber = Receiver()
    interop_parser.add_subscribers(subscriber)
    interop_parser.run()

    def test_read_error_rate(self):
        self.assertListEqual(self.subscriber.error_rate_values,
                             [('error_rate', 
                                {'lane': 1, 
                                 'read': 1, 
                                 'error_rate': 1.5317546129226685}),
                              ('error_rate',
                                {'lane': 1,
                                 'read': 2,
                                 'error_rate': 1.9201501607894897})])


    def test_percent_q30(self):
        self.assertListEqual(self.subscriber.percent_q30_values,
                             [('percent_q30', 
                               {'lane': 1, 
                                'read': 1, 
                                'percent_q30': 93.42070007324219, 
                                'is_index_read': False}),
                              ('percent_q30', 
                               {'lane': 1, 
                                'read': 2, 
                                'percent_q30': 84.4270248413086, 
                                'is_index_read': False})])
        
    def test_percent_q30_per_cycle_r1(self):
         expected_values = {6: 98.76343, 7: 98.718155, 8: 98.529205, 9: 98.43606, 10: 98.41527, 11: 98.35158, 12: 98.37026, 13: 98.38132, 14: 98.36106, 15: 98.335, 16: 98.41815, 17: 98.34947, 18: 98.39447, 19: 98.34131, 20: 98.4179, 21: 98.39527, 22: 98.39079, 23: 98.341324, 24: 98.37368, 25: 98.27342, 26: 98.148155, 27: 98.03079, 28: 98.08657, 29: 98.005005, 30: 98.03605, 31: 97.94395, 32: 98.06053, 33: 97.95342, 34: 98.01316, 35: 98.0458, 36: 98.01947, 37: 98.009735, 38: 98.02342, 39: 97.90763, 40: 97.99262, 41: 97.978424, 42: 97.91369, 43: 97.84553, 44: 97.97316, 45: 97.86104, 46: 97.93341, 47: 97.86342, 48: 97.841576, 49: 97.64315, 50: 97.54816, 51: 97.47948, 52: 97.47237, 53: 97.377106, 54: 97.447105, 55: 97.27185, 56: 97.403946, 57: 97.34501, 58: 97.41447, 59: 97.38974, 60: 97.433426, 61: 97.40026, 62: 97.42869, 63: 97.29763, 64: 97.43052, 65: 97.39132, 66: 97.34763, 67: 97.17079, 68: 97.25579, 69: 97.31422, 70: 97.286575, 71: 97.22263, 72: 97.27711, 73: 97.16738, 74: 97.14105, 75: 96.94316, 76: 97.13577, 77: 96.94395, 78: 97.11817, 79: 96.86737, 80: 97.01237, 81: 96.95684, 82: 96.95264, 83: 97.04738, 84: 97.03184, 85: 97.04105, 86: 96.98684, 87: 96.835, 88: 96.93789, 89: 96.85237, 90: 96.81421, 91: 96.86896, 92: 96.80868, 93: 96.90315, 94: 96.664215, 95: 96.81447, 96: 96.70737, 97: 96.735794, 98: 96.7679, 99: 96.728165, 100: 96.73658, 101: 96.64632, 102: 96.46658, 103: 96.48131, 104: 96.41448, 105: 96.574745, 106: 96.51894, 107: 96.31079, 108: 96.31421, 109: 96.45342, 110: 96.29737, 111: 96.19973, 112: 96.188416, 113: 96.289734, 114: 96.29763, 115: 96.32, 116: 94.81028, 117: 95.52737, 118: 96.005005, 119: 95.86289, 120: 96.17553, 121: 96.218414, 122: 96.27237, 123: 96.23263, 124: 96.3079, 125: 96.18527, 126: 96.22947, 127: 96.21816, 128: 96.259476, 129: 96.14763, 130: 92.26922, 131: 95.46, 132: 95.90264, 133: 95.898415, 134: 94.49395, 135: 95.76396, 136: 95.94606, 137: 95.11658, 138: 95.752106, 139: 95.557106, 140: 95.562355, 141: 95.71289, 142: 95.80552, 143: 95.55026, 144: 93.14158, 145: 95.316055, 146: 95.50447, 147: 95.607635, 148: 95.561844, 149: 95.45895, 150: 95.56026, 151: 94.96788, 152: 95.34317, 153: 95.46264, 154: 95.459465, 155: 95.525536, 156: 95.56736, 157: 95.652885, 158: 95.606316, 159: 95.58342, 160: 95.43131, 161: 95.49342, 162: 95.39658, 163: 95.44184, 164: 95.22317, 165: 95.295265, 166: 95.095535, 167: 95.14896, 168: 94.780525, 169: 94.87027, 170: 94.70605, 171: 94.64394, 172: 94.80764, 173: 94.50131, 174: 94.69448, 175: 94.68158, 176: 94.497375, 177: 94.515785, 178: 94.417366, 179: 94.45975, 180: 94.27211, 181: 94.198685, 182: 94.20026, 183: 94.221565, 184: 93.94553, 185: 93.85895, 186: 93.96526, 187: 94.10264, 188: 93.86763, 189: 93.65447, 190: 93.83105, 191: 93.61816, 192: 93.38394, 193: 93.1437, 194: 93.223946, 195: 91.49342, 196: 92.098946, 197: 92.40526, 198: 92.94052, 199: 87.92157, 200: 90.16184, 201: 90.41526, 202: 91.70974, 203: 92.38053, 204: 92.53263, 205: 92.225266, 206: 92.427635, 207: 92.50421, 208: 92.27869, 209: 92.33895, 210: 92.20184, 211: 92.12736, 212: 92.165794, 213: 92.10736, 214: 92.01763, 215: 91.983955, 216: 91.90525, 217: 91.874214, 218: 91.66367, 219: 91.71869, 220: 91.6671, 221: 91.53262, 222: 91.34948, 223: 91.16526, 224: 91.13737, 225: 90.939735, 226: 91.092384, 227: 90.33316, 228: 90.63632, 229: 90.73973, 230: 90.55527, 231: 90.494995, 232: 90.55237, 233: 90.24158, 234: 90.32605, 235: 90.22631, 236: 89.959465, 237: 89.8784, 238: 89.793945, 239: 89.76474, 240: 89.503426, 241: 89.3421, 242: 89.11763, 243: 89.16948, 244: 88.73395, 245: 88.74973, 246: 88.48079, 247: 88.43711, 248: 88.530525, 249: 88.37474, 250: 88.42394, 251: 88.42105, 252: 88.267105, 253: 88.14474, 254: 87.89184, 255: 87.78474, 256: 87.58157, 257: 87.51632, 258: 87.162094, 259: 87.12895, 260: 86.8392, 261: 86.82895, 262: 86.626854, 263: 86.60184, 264: 86.52368, 265: 86.15026, 266: 86.00895, 267: 86.002625, 268: 85.73631, 269: 85.706055, 270: 85.48342, 271: 85.522896}
         self.assertListEqual(self.subscriber.percent_q30_per_cycle,
                              [('percent_q30_per_cycle', 
                                {'lane': 1, 
                                 'read': 1, 
                                 'percent_q30_per_cycle': expected_values, 
                                 'is_index_read': False})])
        
    # def test_percent_q30_per_cycle_r2(self):
    #     expected_values = {6: 95.20342, 7: 95.16185, 8: 95.1863, 9: 95.170265, 10: 95.203415, 11: 95.21843, 12: 95.27683, 13: 95.26711, 14: 95.22132, 15: 95.35527, 16: 95.32395, 17: 95.30816, 18: 95.320786, 19: 95.13632, 20: 95.163155, 21: 95.19579, 22: 95.12079, 23: 95.09973, 24: 94.0679, 25: 94.97895, 26: 94.98633, 27: 95.07105, 28: 95.145, 29: 95.09499, 30: 95.098946, 31: 94.90711, 32: 95.02474, 33: 95.0, 34: 95.025, 35: 95.04948, 36: 95.03974, 37: 95.0771, 38: 95.01473, 39: 94.98526, 40: 94.996315, 41: 95.0029, 42: 95.04974, 43: 95.003685, 44: 95.07894, 45: 94.98317, 46: 94.98421, 47: 94.79, 48: 94.90026, 49: 94.873955, 50: 94.85027, 51: 94.78448, 52: 94.7971, 53: 94.7679, 54: 94.68052, 55: 94.73683, 56: 94.73869, 57: 94.73946, 58: 94.6442, 59: 94.57448, 60: 94.66605, 61: 94.58527, 62: 94.12632, 63: 94.470535, 64: 94.26341, 65: 94.280785, 66: 94.345795, 67: 93.54104, 68: 94.1479, 69: 94.29315, 70: 94.26132, 71: 94.29973, 72: 94.184204, 73: 94.20526, 74: 94.27, 75: 94.162636, 76: 94.18895, 77: 94.18422, 78: 94.099464, 79: 94.06368, 80: 93.94764, 81: 93.838684, 82: 93.98341, 83: 93.94395, 84: 93.91238, 85: 93.80894, 86: 93.85606, 87: 93.84789, 88: 93.91, 89: 93.823685, 90: 93.859474, 91: 93.743675, 92: 93.76737, 93: 93.65316, 94: 93.75921, 95: 93.63869, 96: 93.40158, 97: 93.462906, 98: 93.45474, 99: 93.37921, 100: 93.10394, 101: 93.20184, 102: 93.05973, 103: 92.87052, 104: 93.03921, 105: 92.621056, 106: 92.93027, 107: 93.00027, 108: 93.01631, 109: 92.90501, 110: 92.913414, 111: 92.98078, 112: 92.860535, 113: 92.82578, 114: 92.54973, 115: 92.84658, 116: 92.765785, 117: 92.80552, 118: 92.80553, 119: 92.88922, 120: 92.67527, 121: 92.71262, 122: 92.79605, 123: 92.91737, 124: 92.7442, 125: 92.62921, 126: 92.77421, 127: 92.75053, 128: 92.586044, 129: 92.66026, 130: 92.5058, 131: 92.43474, 132: 92.23999, 133: 92.084206, 134: 92.165794, 135: 92.2129, 136: 92.24368, 137: 92.213684, 138: 92.25291, 139: 92.07868, 140: 91.970795, 141: 92.05682, 142: 91.94264, 143: 91.83236, 144: 91.79289, 145: 91.827896, 146: 91.62421, 147: 91.46474, 148: 91.57948, 149: 89.09658, 150: 90.12026, 151: 90.84816, 152: 90.96869, 153: 91.10263, 154: 90.96763, 155: 91.088425, 156: 90.85606, 157: 90.90025, 158: 90.65078, 159: 90.61763, 160: 90.52395, 161: 90.37473, 162: 90.329216, 163: 90.19474, 164: 90.19447, 165: 90.122635, 166: 90.10816, 167: 89.93896, 168: 89.759995, 169: 89.792114, 170: 89.676575, 171: 89.53236, 172: 89.4121, 173: 89.48209, 174: 89.39079, 175: 89.19921, 176: 88.7679, 177: 89.023155, 178: 88.92104, 179: 89.01237, 180: 88.68895, 181: 88.73948, 182: 88.60342, 183: 88.40631, 184: 88.0642, 185: 88.17869, 186: 88.00447, 187: 87.980255, 188: 87.78, 189: 87.74895, 190: 87.40341, 191: 87.328674, 192: 87.278946, 193: 87.17237, 194: 87.09789, 195: 86.93525, 196: 86.656845, 197: 86.61606, 198: 86.44842, 199: 86.24947, 200: 86.090515, 201: 86.072365, 202: 85.85422, 203: 85.81816, 204: 85.54027, 205: 85.612366, 206: 85.3679, 207: 85.121315, 208: 84.96552, 209: 84.792625, 210: 84.51894, 211: 84.18474, 212: 84.08395, 213: 83.95052, 214: 83.76157, 215: 83.42079, 216: 83.260796, 217: 83.01658, 218: 82.87078, 219: 82.68711, 220: 82.29868, 221: 82.00869, 222: 81.96079, 223: 81.45843, 224: 81.207375, 225: 80.90316, 226: 80.75053, 227: 80.497635, 228: 79.859215, 229: 79.28025, 230: 79.16685, 231: 78.918945, 232: 78.57159, 233: 78.289474, 234: 78.203674, 235: 77.89342, 236: 77.598946, 237: 77.09841, 238: 77.01184, 239: 76.68105, 240: 76.517105, 241: 76.051315, 242: 75.56605, 243: 75.295, 244: 74.86473, 245: 74.64579, 246: 74.09158, 247: 73.68289, 248: 73.48212, 249: 73.09475, 250: 69.588684, 251: 68.71553, 252: 69.6721, 253: 70.78684, 254: 69.506584, 255: 69.116844, 256: 67.87816, 257: 67.40921, 258: 67.396835, 259: 67.61025, 260: 67.024216, 261: 66.58738, 262: 65.98212, 263: 65.24343, 264: 64.43105, 265: 63.750534, 266: 59.648426, 267: 59.842106, 268: 60.35448, 269: 61.38657, 270: 61.0029, 271: 60.440525}
    #     self.assertListEqual(self.subscriber.percent_q30_per_cycle,
    #                          [('percent_q30_per_cycle', 
    #                            {'lane': 1, 
    #                             'read': 2, 
    #                             'percent_q30_per_cycle': expected_values, 
    #                             'is_index_read': False})])
    
    def test_get_percent_q30_per_cycle(self):
        runfolder = os.path.join(os.path.dirname(__file__), "..", 
                             "resources", 
                             "MiSeqDemo")
 
        q_metrics = imaging(runfolder,
              valid_to_load=['Q'])
        
        get_q30_call_as_var = InteropParser.get_percent_q30_per_cycle(
                q_metrics=q_metrics,
                lane_nr=0, 
                read_nr=0,
                is_index_read=False)

        expected_out = {
                6: 98.76343,
                48: 97.841576,
                90: 96.81421,
                132: 95.90264,
                174: 94.69448,
                216: 91.90525,
                258: 87.162094,
        }

        filtered_dict = {
            cycle: get_q30_call_as_var[cycle]
            for cycle in expected_out
        }

        for cycle in filtered_dict:
            self.assertTrue(np.isclose(
                expected_out[cycle], filtered_dict[cycle]))
