from .arch import Arch
from .archerror import ArchError

class ArchS7XX(Arch):
    def __init__(self, endness='Iend_BE'):
        if endness == 'Iend_LE':
            raise ArchError('Arch S7XX must be little endian')
        super(ArchS7XX, self).__init__(endness)

    bits = 32
    vex_arch = "VexArchS7XX"
    name = "S7XX"
    cs_mode = None
    memory_endness = "Iend_BE"
    register_endness = "Iend_BE"
    ret_instruction = "\x05\x00"  # BE
    nop_instruction = "\x00\x00"  # NOP
    instruction_alignment = 1
    default_register_values = [
        ( 'ACCU1', 0, True, None ), 
        ( 'ACCU2', 0, True, None ),
        ( 'PWD', 0, True, None),
        ( 'DB', 0, True, None),
        ( 'DI', 0, True, None)
    ]

    default_symbolic_registers = [ 'ACCU1', 'ACCU2', 'PWD', 'AR1', 'AR2', 'DB', 'DI' ]
    register_names = {
        8: 'ACCU1',
        12: 'ACCU2',
        16: 'PWD',
        20: 'AR1', 
        24: 'AR2'
    }

    registers = {
        'eax': (8, 4),
        'ecx': (12, 4),
        'edx': (16, 4),
        'ebx': (20, 4),

        'sp': (24, 4),
        'esp': (24, 4),

        'ebp': (28, 4), 'bp': (28, 4),
        'esi': (32, 4),
        'edi': (36, 4),

        # condition stuff
        'cc_op': (40, 4),
        'cc_dep1': (44, 4),
        'cc_dep2': (48, 4),
        'cc_ndep': (52, 4),

        # this determines which direction SSE instructions go
        'd': (56, 4),

        # separately-stored bits of eflags
        'id': (60, 4),
        'ac': (64, 4),

        'eip': (68, 4),
        'pc': (68, 4),
        'ip': (68, 4),

        # fpu registers and mmx aliases
        'fpu_regs': (72, 64),
        'st0': (72, 8),
        'st1': (80, 8),
        'st2': (88, 8),
        'st3': (96, 8),
        'st4': (104, 8),
        'st5': (112, 8),
        'st6': (120, 8),
        'st7': (128, 8),
        'mm0': (72, 8),
        'mm1': (80, 8),
        'mm2': (88, 8),
        'mm3': (96, 8),
        'mm4': (104, 8),
        'mm5': (112, 8),
        'mm6': (120, 8),
        'mm7': (128, 8),

        # fpu tags
        'fpu_tags': (136, 8),
        'fpu_t0': (136, 1),
        'fpu_t1': (137, 1),
        'fpu_t2': (138, 1),
        'fpu_t3': (139, 1),
        'fpu_t4': (140, 1),
        'fpu_t5': (141, 1),
        'fpu_t6': (142, 1),
        'fpu_t7': (143, 1),

        # fpu settings
        'fpround': (144, 4),
        'fc3210': (148, 4),
        'ftop': (152, 4),

        # sse
        'sseround': (156, 4),
        'xmm0': (160, 16),
        'xmm1': (176, 16),
        'xmm2': (192, 16),
        'xmm3': (208, 16),
        'xmm4': (224, 16),
        'xmm5': (240, 16),
        'xmm6': (256, 16),
        'xmm7': (272, 16),

        'cs': (288, 2),
        'ds': (290, 2),
        'es': (292, 2),
        'fs': (294, 2),
        'gs': (296, 2),
        'ss': (298, 2),
        'ldt': (304, 8),
        'gdt': (312, 8)
    }

