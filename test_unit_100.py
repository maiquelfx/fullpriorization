# -*- coding: utf-8 -*-
#cd C:\caminho
# python -m pytest -v test_arquivo > output.txt // para gerar o output.txt

import pytest
from main import Calc

dicio = {}

pond_comp = 0.30
pond_risco = 0.50
pond_prazo = 0.20

def calc():
    result = (pond_comp * complexidade + pond_risco * risco + prazo * pond_prazo)
    return result

# teste 1
complexidade=5
risco=2
prazo=2
dicio['t1'] = calc()

# teste 2
complexidade=2
risco=5
prazo=5
dicio['t2'] = calc()

# teste 3
complexidade=5
risco=4
prazo=4
dicio['t3'] = calc()

# teste 4
complexidade=2
risco=5
prazo=5
dicio['t4'] = calc()

# teste 5
complexidade=3
risco=2
prazo=2
dicio['t5'] = calc()

# teste 6
complexidade=2
risco=1
prazo=1
dicio['t6'] = calc()

# teste 7
complexidade=1
risco=4
prazo=4
dicio['t7'] = calc()

# teste 8
complexidade=3
risco=3
prazo=3
dicio['t8'] = calc()

# teste 9
complexidade=4
risco=4
prazo=4
dicio['t9'] = calc()

# teste 10
complexidade=1
risco=4
prazo=4
dicio['t10'] = calc()

# teste 11
complexidade=3
risco=1
prazo=1
dicio['t11'] = calc()

# teste 12
complexidade=5
risco=1
prazo=1
dicio['t12'] = calc()

# teste 13
complexidade=1
risco=2
prazo=2
dicio['t13'] = calc()

# teste 14
complexidade=1
risco=4
prazo=4
dicio['t14'] = calc()

# teste 15
complexidade=4
risco=5
prazo=5
dicio['t15'] = calc()

# teste 16
complexidade=2
risco=2
prazo=2
dicio['t16'] = calc()

# teste 17
complexidade=5
risco=4
prazo=4
dicio['t17'] = calc()

# teste 18
complexidade=5
risco=2
prazo=2
dicio['t18'] = calc()

# teste 19
complexidade=5
risco=2
prazo=2
dicio['t19'] = calc()

# teste 20
complexidade=5
risco=5
prazo=5
dicio['t20'] = calc()

# teste 21
complexidade=5
risco=3
prazo=3
dicio['t21'] = calc()

# teste 22
complexidade=3
risco=1
prazo=1
dicio['t22'] = calc()

# teste 23
complexidade=4
risco=5
prazo=5
dicio['t23'] = calc()

# teste 24
complexidade=5
risco=4
prazo=4
dicio['t24'] = calc()

# teste 25
complexidade=1
risco=4
prazo=4
dicio['t25'] = calc()

# teste 26
complexidade=1
risco=2
prazo=2
dicio['t26'] = calc()

# teste 27
complexidade=5
risco=4
prazo=4
dicio['t27'] = calc()

# teste 28
complexidade=1
risco=5
prazo=5
dicio['t28'] = calc()

# teste 29
complexidade=1
risco=5
prazo=5
dicio['t29'] = calc()

# teste 30
complexidade=3
risco=1
prazo=1
dicio['t30'] = calc()

# teste 31
complexidade=2
risco=1
prazo=1
dicio['t31'] = calc()

# teste 32
complexidade=4
risco=1
prazo=1
dicio['t32'] = calc()

# teste 33
complexidade=4
risco=1
prazo=1
dicio['t33'] = calc()

# teste 34
complexidade=3
risco=3
prazo=3
dicio['t34'] = calc()

# teste 35
complexidade=1
risco=2
prazo=2
dicio['t35'] = calc()

# teste 36
complexidade=3
risco=5
prazo=5
dicio['t36'] = calc()

# teste 37
complexidade=1
risco=3
prazo=3
dicio['t37'] = calc()

# teste 38
complexidade=2
risco=2
prazo=2
dicio['t38'] = calc()

# teste 39
complexidade=1
risco=4
prazo=4
dicio['t39'] = calc()

# teste 40
complexidade=4
risco=3
prazo=3
dicio['t40'] = calc()

# teste 41
complexidade=1
risco=3
prazo=3
dicio['t41'] = calc()

# teste 42
complexidade=3
risco=3
prazo=3
dicio['t42'] = calc()

# teste 43
complexidade=1
risco=2
prazo=2
dicio['t43'] = calc()

# teste 44
complexidade=1
risco=2
prazo=2
dicio['t44'] = calc()

# teste 45
complexidade=2
risco=1
prazo=1
dicio['t45'] = calc()

# teste 46
complexidade=1
risco=4
prazo=4
dicio['t46'] = calc()

# teste 47
complexidade=2
risco=1
prazo=1
dicio['t47'] = calc()

# teste 48
complexidade=3
risco=4
prazo=4
dicio['t48'] = calc()

# teste 49
complexidade=5
risco=4
prazo=4
dicio['t49'] = calc()

# teste 50
complexidade=5
risco=3
prazo=3
dicio['t50'] = calc()

# teste 51
complexidade=5
risco=3
prazo=3
dicio['t51'] = calc()

# teste 52
complexidade=2
risco=4
prazo=4
dicio['t52'] = calc()

# teste 53
complexidade=1
risco=2
prazo=2
dicio['t53'] = calc()

# teste 54
complexidade=4
risco=3
prazo=3
dicio['t54'] = calc()

# teste 55
complexidade=2
risco=3
prazo=3
dicio['t55'] = calc()

# teste 56
complexidade=4
risco=3
prazo=3
dicio['t56'] = calc()

# teste 57
complexidade=1
risco=3
prazo=3
dicio['t57'] = calc()

# teste 58
complexidade=2
risco=3
prazo=3
dicio['t58'] = calc()

# teste 59
complexidade=3
risco=1
prazo=1
dicio['t59'] = calc()

# teste 60
complexidade=3
risco=2
prazo=2
dicio['t60'] = calc()

# teste 61
complexidade=3
risco=3
prazo=3
dicio['t61'] = calc()

# teste 62
complexidade=5
risco=1
prazo=1
dicio['t62'] = calc()

# teste 63
complexidade=3
risco=1
prazo=1
dicio['t63'] = calc()

# teste 64
complexidade=4
risco=1
prazo=1
dicio['t64'] = calc()

# teste 65
complexidade=5
risco=5
prazo=5
dicio['t65'] = calc()

# teste 66
complexidade=5
risco=3
prazo=3
dicio['t66'] = calc()

# teste 67
complexidade=4
risco=5
prazo=5
dicio['t67'] = calc()

# teste 68
complexidade=1
risco=2
prazo=2
dicio['t68'] = calc()

# teste 69
complexidade=1
risco=4
prazo=4
dicio['t69'] = calc()

# teste 70
complexidade=5
risco=4
prazo=4
dicio['t70'] = calc()

# teste 71
complexidade=4
risco=2
prazo=2
dicio['t71'] = calc()

# teste 72
complexidade=4
risco=3
prazo=3
dicio['t72'] = calc()

# teste 73
complexidade=1
risco=5
prazo=5
dicio['t73'] = calc()

# teste 74
complexidade=1
risco=4
prazo=4
dicio['t74'] = calc()

# teste 75
complexidade=1
risco=1
prazo=1
dicio['t75'] = calc()

# teste 76
complexidade=2
risco=3
prazo=3
dicio['t76'] = calc()

# teste 77
complexidade=1
risco=3
prazo=3
dicio['t77'] = calc()

# teste 78
complexidade=4
risco=3
prazo=3
dicio['t78'] = calc()

# teste 79
complexidade=2
risco=1
prazo=1
dicio['t79'] = calc()

# teste 80
complexidade=5
risco=1
prazo=1
dicio['t80'] = calc()

# teste 81
complexidade=1
risco=3
prazo=3
dicio['t81'] = calc()

# teste 82
complexidade=3
risco=1
prazo=1
dicio['t82'] = calc()

# teste 83
complexidade=2
risco=4
prazo=4
dicio['t83'] = calc()

# teste 84
complexidade=3
risco=5
prazo=5
dicio['t84'] = calc()

# teste 85
complexidade=1
risco=5
prazo=5
dicio['t85'] = calc()

# teste 86
complexidade=4
risco=1
prazo=1
dicio['t86'] = calc()

# teste 87
complexidade=2
risco=3
prazo=3
dicio['t87'] = calc()

# teste 88
complexidade=1
risco=3
prazo=3
dicio['t88'] = calc()

# teste 89
complexidade=3
risco=5
prazo=5
dicio['t89'] = calc()

# teste 90
complexidade=2
risco=1
prazo=1
dicio['t90'] = calc()

# teste 91
complexidade=2
risco=4
prazo=4
dicio['t91'] = calc()

# teste 92
complexidade=5
risco=4
prazo=4
dicio['t92'] = calc()

# teste 93
complexidade=3
risco=4
prazo=4
dicio['t93'] = calc()

# teste 94
complexidade=5
risco=5
prazo=5
dicio['t94'] = calc()

# teste 95
complexidade=5
risco=3
prazo=3
dicio['t95'] = calc()

# teste 96
complexidade=1
risco=4
prazo=4
dicio['t96'] = calc()

# teste 97
complexidade=1
risco=4
prazo=4
dicio['t97'] = calc()

# teste 98
complexidade=2
risco=2
prazo=2
dicio['t98'] = calc()

# teste 99
complexidade=4
risco=5
prazo=5
dicio['t99'] = calc()

# teste 100
complexidade=1
risco=5
prazo=5
dicio['t100'] = calc()




# Crie uma lista ordenada de valores únicos das ordens
ordens_ordenadas = sorted(set(dicio.values()), reverse=True)

# Crie um novo dicionário com as ordens atualizadas
novo_dicio = {}
ordem = 0

for teste, ordem_original in sorted(dicio.items(), key=lambda x: x[1], reverse=True):
    novo_dicio[teste] = ordens_ordenadas.index(ordem_original)


class TestCalc:
    def setup_method(self):
        self.inst = Calc()

    # Teste 1
    @pytest.mark.run(order=novo_dicio.get('t1', 0))    
    def test_equal_1(self):
        assert self.inst.equal(98, 6) == 104

    # Teste 2
    @pytest.mark.run(order=novo_dicio.get('t2', 0))    
    def test_equal_2(self):
        assert self.inst.equal(30, 11) == 41

    # Teste 3
    @pytest.mark.run(order=novo_dicio.get('t3', 0))    
    def test_equal_3(self):
        assert self.inst.equal(85, 3) == 88

    # Teste 4
    @pytest.mark.run(order=novo_dicio.get('t4', 0))    
    def test_equal_4(self):
        assert self.inst.equal(75, 17) == 92

    # Teste 5
    @pytest.mark.run(order=novo_dicio.get('t5', 0))    
    def test_equal_5(self):
        assert self.inst.equal(28, 74) == 102

    # Teste 6
    @pytest.mark.run(order=novo_dicio.get('t6', 0))    
    def test_equal_6(self):
        assert self.inst.equal(52, 1) == 53

    # Teste 7
    @pytest.mark.run(order=novo_dicio.get('t7', 0))    
    def test_equal_7(self):
        assert self.inst.equal(83, 78) == 161

    # Teste 8
    @pytest.mark.run(order=novo_dicio.get('t8', 0))    
    def test_equal_8(self):
        assert self.inst.equal(95, 74) == 169

    # Teste 9
    @pytest.mark.run(order=novo_dicio.get('t9', 0))    
    def test_equal_9(self):
        assert self.inst.equal(80, 68) == 148

    # Teste 10
    @pytest.mark.run(order=novo_dicio.get('t10', 0))    
    def test_equal_10(self):
        assert self.inst.equal(37, 63) == 100

    # Teste 11
    @pytest.mark.run(order=novo_dicio.get('t11', 0))    
    def test_equal_11(self):
        assert self.inst.equal(65, 65) == 130

    # Teste 12
    @pytest.mark.run(order=novo_dicio.get('t12', 0))    
    def test_equal_12(self):
        assert self.inst.equal(47, 13) == 60

    # Teste 13
    @pytest.mark.run(order=novo_dicio.get('t13', 0))    
    def test_equal_13(self):
        assert self.inst.equal(72, 21) == 93

    # Teste 14
    @pytest.mark.run(order=novo_dicio.get('t14', 0))    
    def test_equal_14(self):
        assert self.inst.equal(55, 7) == 62

    # Teste 15
    @pytest.mark.run(order=novo_dicio.get('t15', 0))    
    def test_equal_15(self):
        assert self.inst.equal(75, 10) == 850

    # Teste 16
    @pytest.mark.run(order=novo_dicio.get('t16', 0))    
    def test_equal_16(self):
        assert self.inst.equal(6, 96) == 102

    # Teste 17
    @pytest.mark.run(order=novo_dicio.get('t17', 0))    
    def test_equal_17(self):
        assert self.inst.equal(86, 0) == 86

    # Teste 18
    @pytest.mark.run(order=novo_dicio.get('t18', 0))    
    def test_equal_18(self):
        assert self.inst.equal(70, 47) == 117

    # Teste 19
    @pytest.mark.run(order=novo_dicio.get('t19', 0))    
    def test_equal_19(self):
        assert self.inst.equal(6, 37) == 43

    # Teste 20
    @pytest.mark.run(order=novo_dicio.get('t20', 0))    
    def test_equal_20(self):
        assert self.inst.equal(93, 11) == 104

    # Teste 21
    @pytest.mark.run(order=novo_dicio.get('t21', 0))    
    def test_equal_21(self):
        assert self.inst.equal(2, 58) == 60

    # Teste 22
    @pytest.mark.run(order=novo_dicio.get('t22', 0))    
    def test_equal_22(self):
        assert self.inst.equal(24, 97) == 121

    # Teste 23
    @pytest.mark.run(order=novo_dicio.get('t23', 0))    
    def test_equal_23(self):
        assert self.inst.equal(19, 16) == 35

    # Teste 24
    @pytest.mark.run(order=novo_dicio.get('t24', 0))    
    def test_equal_24(self):
        assert self.inst.equal(58, 15) == 730

    # Teste 25
    @pytest.mark.run(order=novo_dicio.get('t25', 0))    
    def test_equal_25(self):
        assert self.inst.equal(24, 0) == 24

    # Teste 26
    @pytest.mark.run(order=novo_dicio.get('t26', 0))    
    def test_equal_26(self):
        assert self.inst.equal(57, 75) == 132

    # Teste 27
    @pytest.mark.run(order=novo_dicio.get('t27', 0))    
    def test_equal_27(self):
        assert self.inst.equal(33, 97) == 1300

    # Teste 28
    @pytest.mark.run(order=novo_dicio.get('t28', 0))    
    def test_equal_28(self):
        assert self.inst.equal(48, 30) == 78

    # Teste 29
    @pytest.mark.run(order=novo_dicio.get('t29', 0))    
    def test_equal_29(self):
        assert self.inst.equal(45, 20) == 65

    # Teste 30
    @pytest.mark.run(order=novo_dicio.get('t30', 0))    
    def test_equal_30(self):
        assert self.inst.equal(32, 39) == 71

    # Teste 31
    @pytest.mark.run(order=novo_dicio.get('t31', 0))    
    def test_equal_31(self):
        assert self.inst.equal(18, 74) == 92

    # Teste 32
    @pytest.mark.run(order=novo_dicio.get('t32', 0))    
    def test_equal_32(self):
        assert self.inst.equal(46, 97) == 143

    # Teste 33
    @pytest.mark.run(order=novo_dicio.get('t33', 0))    
    def test_equal_33(self):
        assert self.inst.equal(87, 9) == 96

    # Teste 34
    @pytest.mark.run(order=novo_dicio.get('t34', 0))    
    def test_equal_34(self):
        assert self.inst.equal(45, 65) == 110

    # Teste 35
    @pytest.mark.run(order=novo_dicio.get('t35', 0))    
    def test_equal_35(self):
        assert self.inst.equal(88, 4) == 92

    # Teste 36
    @pytest.mark.run(order=novo_dicio.get('t36', 0))    
    def test_equal_36(self):
        assert self.inst.equal(44, 73) == 117

    # Teste 37
    @pytest.mark.run(order=novo_dicio.get('t37', 0))    
    def test_equal_37(self):
        assert self.inst.equal(9, 31) == 40

    # Teste 38
    @pytest.mark.run(order=novo_dicio.get('t38', 0))    
    def test_equal_38(self):
        assert self.inst.equal(78, 32) == 110

    # Teste 39
    @pytest.mark.run(order=novo_dicio.get('t39', 0))    
    def test_equal_39(self):
        assert self.inst.equal(21, 28) == 49

    # Teste 40
    @pytest.mark.run(order=novo_dicio.get('t40', 0))    
    def test_equal_40(self):
        assert self.inst.equal(96, 47) == 143

    # Teste 41
    @pytest.mark.run(order=novo_dicio.get('t41', 0))    
    def test_equal_41(self):
        assert self.inst.equal(1, 8) == 9

    # Teste 42
    @pytest.mark.run(order=novo_dicio.get('t42', 0))    
    def test_equal_42(self):
        assert self.inst.equal(77, 26) == 103

    # Teste 43
    @pytest.mark.run(order=novo_dicio.get('t43', 0))    
    def test_equal_43(self):
        assert self.inst.equal(74, 49) == 123

    # Teste 44
    @pytest.mark.run(order=novo_dicio.get('t44', 0))    
    def test_equal_44(self):
        assert self.inst.equal(15, 6) == 21

    # Teste 45
    @pytest.mark.run(order=novo_dicio.get('t45', 0))    
    def test_equal_45(self):
        assert self.inst.equal(67, 33) == 100

    # Teste 46
    @pytest.mark.run(order=novo_dicio.get('t46', 0))    
    def test_equal_46(self):
        assert self.inst.equal(17, 16) == 33

    # Teste 47
    @pytest.mark.run(order=novo_dicio.get('t47', 0))    
    def test_equal_47(self):
        assert self.inst.equal(57, 90) == 147

    # Teste 48
    @pytest.mark.run(order=novo_dicio.get('t48', 0))    
    def test_equal_48(self):
        assert self.inst.equal(99, 67) == 166

    # Teste 49
    @pytest.mark.run(order=novo_dicio.get('t49', 0))    
    def test_equal_49(self):
        assert self.inst.equal(6, 0) == 6

    # Teste 50
    @pytest.mark.run(order=novo_dicio.get('t50', 0))    
    def test_equal_50(self):
        assert self.inst.equal(61, 67) == 128

    # Teste 51
    @pytest.mark.run(order=novo_dicio.get('t51', 0))    
    def test_equal_51(self):
        assert self.inst.equal(36, 27) == 63

    # Teste 52
    @pytest.mark.run(order=novo_dicio.get('t52', 0))    
    def test_equal_52(self):
        assert self.inst.equal(76, 87) == 163

    # Teste 53
    @pytest.mark.run(order=novo_dicio.get('t53', 0))    
    def test_equal_53(self):
        assert self.inst.equal(58, 71) == 129

    # Teste 54
    @pytest.mark.run(order=novo_dicio.get('t54', 0))    
    def test_equal_54(self):
        assert self.inst.equal(65, 16) == 81

    # Teste 55
    @pytest.mark.run(order=novo_dicio.get('t55', 0))    
    def test_equal_55(self):
        assert self.inst.equal(18, 35) == 53

    # Teste 56
    @pytest.mark.run(order=novo_dicio.get('t56', 0))    
    def test_equal_56(self):
        assert self.inst.equal(58, 56) == 114

    # Teste 57
    @pytest.mark.run(order=novo_dicio.get('t57', 0))    
    def test_equal_57(self):
        assert self.inst.equal(37, 42) == 79

    # Teste 58
    @pytest.mark.run(order=novo_dicio.get('t58', 0))    
    def test_equal_58(self):
        assert self.inst.equal(35, 63) == 98

    # Teste 59
    @pytest.mark.run(order=novo_dicio.get('t59', 0))    
    def test_equal_59(self):
        assert self.inst.equal(68, 75) == 143

    # Teste 60
    @pytest.mark.run(order=novo_dicio.get('t60', 0))    
    def test_equal_60(self):
        assert self.inst.equal(46, 39) == 85

    # Teste 61
    @pytest.mark.run(order=novo_dicio.get('t61', 0))    
    def test_equal_61(self):
        assert self.inst.equal(93, 43) == 136

    # Teste 62
    @pytest.mark.run(order=novo_dicio.get('t62', 0))    
    def test_equal_62(self):
        assert self.inst.equal(24, 37) == 61

    # Teste 63
    @pytest.mark.run(order=novo_dicio.get('t63', 0))    
    def test_equal_63(self):
        assert self.inst.equal(87, 29) == 116

    # Teste 64
    @pytest.mark.run(order=novo_dicio.get('t64', 0))    
    def test_equal_64(self):
        assert self.inst.equal(99, 19) == 118

    # Teste 65
    @pytest.mark.run(order=novo_dicio.get('t65', 0))    
    def test_equal_65(self):
        assert self.inst.equal(49, 10) == 59

    # Teste 66
    @pytest.mark.run(order=novo_dicio.get('t66', 0))    
    def test_equal_66(self):
        assert self.inst.equal(14, 56) == 70

    # Teste 67
    @pytest.mark.run(order=novo_dicio.get('t67', 0))    
    def test_equal_67(self):
        assert self.inst.equal(7, 10) == 170

    # Teste 68
    @pytest.mark.run(order=novo_dicio.get('t68', 0))    
    def test_equal_68(self):
        assert self.inst.equal(69, 11) == 80

    # Teste 69
    @pytest.mark.run(order=novo_dicio.get('t69', 0))    
    def test_equal_69(self):
        assert self.inst.equal(64, 34) == 98

    # Teste 70
    @pytest.mark.run(order=novo_dicio.get('t70', 0))    
    def test_equal_70(self):
        assert self.inst.equal(66, 3) == 69

    # Teste 71
    @pytest.mark.run(order=novo_dicio.get('t71', 0))    
    def test_equal_71(self):
        assert self.inst.equal(39, 58) == 97

    # Teste 72
    @pytest.mark.run(order=novo_dicio.get('t72', 0))    
    def test_equal_72(self):
        assert self.inst.equal(17, 69) == 86

    # Teste 73
    @pytest.mark.run(order=novo_dicio.get('t73', 0))    
    def test_equal_73(self):
        assert self.inst.equal(1, 39) == 40

    # Teste 74
    @pytest.mark.run(order=novo_dicio.get('t74', 0))    
    def test_equal_74(self):
        assert self.inst.equal(96, 66) == 162

    # Teste 75
    @pytest.mark.run(order=novo_dicio.get('t75', 0))    
    def test_equal_75(self):
        assert self.inst.equal(52, 79) == 131

    # Teste 76
    @pytest.mark.run(order=novo_dicio.get('t76', 0))    
    def test_equal_76(self):
        assert self.inst.equal(11, 97) == 108

    # Teste 77
    @pytest.mark.run(order=novo_dicio.get('t77', 0))    
    def test_equal_77(self):
        assert self.inst.equal(46, 65) == 111

    # Teste 78
    @pytest.mark.run(order=novo_dicio.get('t78', 0))    
    def test_equal_78(self):
        assert self.inst.equal(40, 47) == 87

    # Teste 79
    @pytest.mark.run(order=novo_dicio.get('t79', 0))    
    def test_equal_79(self):
        assert self.inst.equal(39, 65) == 104

    # Teste 80
    @pytest.mark.run(order=novo_dicio.get('t80', 0))    
    def test_equal_80(self):
        assert self.inst.equal(23, 47) == 70

    # Teste 81
    @pytest.mark.run(order=novo_dicio.get('t81', 0))    
    def test_equal_81(self):
        assert self.inst.equal(29, 10) == 39

    # Teste 82
    @pytest.mark.run(order=novo_dicio.get('t82', 0))    
    def test_equal_82(self):
        assert self.inst.equal(41, 60) == 101

    # Teste 83
    @pytest.mark.run(order=novo_dicio.get('t83', 0))    
    def test_equal_83(self):
        assert self.inst.equal(35, 95) == 130

    # Teste 84
    @pytest.mark.run(order=novo_dicio.get('t84', 0))    
    def test_equal_84(self):
        assert self.inst.equal(29, 85) == 1140

    # Teste 85
    @pytest.mark.run(order=novo_dicio.get('t85', 0))    
    def test_equal_85(self):
        assert self.inst.equal(19, 81) == 100

    # Teste 86
    @pytest.mark.run(order=novo_dicio.get('t86', 0))    
    def test_equal_86(self):
        assert self.inst.equal(69, 55) == 124

    # Teste 87
    @pytest.mark.run(order=novo_dicio.get('t87', 0))    
    def test_equal_87(self):
        assert self.inst.equal(39, 48) == 87

    # Teste 88
    @pytest.mark.run(order=novo_dicio.get('t88', 0))    
    def test_equal_88(self):
        assert self.inst.equal(95, 83) == 178

    # Teste 89
    @pytest.mark.run(order=novo_dicio.get('t89', 0))    
    def test_equal_89(self):
        assert self.inst.equal(16, 68) == 84

    # Teste 90
    @pytest.mark.run(order=novo_dicio.get('t90', 0))    
    def test_equal_90(self):
        assert self.inst.equal(82, 39) == 121

    # Teste 91
    @pytest.mark.run(order=novo_dicio.get('t91', 0))    
    def test_equal_91(self):
        assert self.inst.equal(40, 61) == 101

    # Teste 92
    @pytest.mark.run(order=novo_dicio.get('t92', 0))    
    def test_equal_92(self):
        assert self.inst.equal(58, 5) == 63

    # Teste 93
    @pytest.mark.run(order=novo_dicio.get('t93', 0))    
    def test_equal_93(self):
        assert self.inst.equal(3, 40) == 43

    # Teste 94
    @pytest.mark.run(order=novo_dicio.get('t94', 0))    
    def test_equal_94(self):
        assert self.inst.equal(40, 76) == 116

    # Teste 95
    @pytest.mark.run(order=novo_dicio.get('t95', 0))    
    def test_equal_95(self):
        assert self.inst.equal(76, 38) == 114

    # Teste 96
    @pytest.mark.run(order=novo_dicio.get('t96', 0))    
    def test_equal_96(self):
        assert self.inst.equal(33, 74) == 107

    # Teste 97
    @pytest.mark.run(order=novo_dicio.get('t97', 0))    
    def test_equal_97(self):
        assert self.inst.equal(70, 36) == 106

    # Teste 98
    @pytest.mark.run(order=novo_dicio.get('t98', 0))    
    def test_equal_98(self):
        assert self.inst.equal(87, 99) == 186

    # Teste 99
    @pytest.mark.run(order=novo_dicio.get('t99', 0))    
    def test_equal_99(self):
        assert self.inst.equal(46, 13) == 59

    # Teste 100
    @pytest.mark.run(order=novo_dicio.get('t100', 0))    
    def test_equal_100(self):
        assert self.inst.equal(28, 81) == 109

