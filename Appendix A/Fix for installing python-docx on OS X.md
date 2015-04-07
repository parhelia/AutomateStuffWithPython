geococcyx:~ brisance$ pip3 install python-docx
Collecting python-docx
  Using cached python-docx-0.8.5.tar.gz
Collecting lxml>=2.3.2 (from python-docx)
  Using cached lxml-3.4.2.tar.gz
    Building lxml version 3.4.2.
    Building without Cython.
    Using build configuration of libxslt 1.1.28
    /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/distutils/dist.py:260: UserWarning: Unknown distribution option: 'bugtrack_url'
      warnings.warn(msg)
Installing collected packages: lxml, python-docx
  Running setup.py install for lxml
    Building lxml version 3.4.2.
    Building without Cython.
    Using build configuration of libxslt 1.1.28
    building 'lxml.etree' extension
    /usr/bin/clang -fno-strict-aliasing -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -arch i386 -arch x86_64 -g -I/usr/include/libxml2 -I/private/var/folders/hb/b19w4_rj14g_1736v__dgg480000gn/T/pip-build-q1dh8_wz/lxml/src/lxml/includes -I/Library/Frameworks/Python.framework/Versions/3.4/include/python3.4m -c src/lxml/lxml.etree.c -o build/temp.macosx-10.6-intel-3.4/src/lxml/lxml.etree.o -w -flat_namespace
    In file included from src/lxml/lxml.etree.c:239:
    /private/var/folders/hb/b19w4_rj14g_1736v__dgg480000gn/T/pip-build-q1dh8_wz/lxml/src/lxml/includes/etree_defs.h:14:10: fatal error: 'libxml/xmlversion.h' file not found
    #include "libxml/xmlversion.h"
             ^
    1 error generated.
    /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/distutils/dist.py:260: UserWarning: Unknown distribution option: 'bugtrack_url'
      warnings.warn(msg)
    error: command '/usr/bin/clang' failed with exit status 1
    Complete output from command /Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4 -c "import setuptools, tokenize;__file__='/private/var/folders/hb/b19w4_rj14g_1736v__dgg480000gn/T/pip-build-q1dh8_wz/lxml/setup.py';exec(compile(getattr(tokenize, 'open', open)(__file__).read().replace('\r\n', '\n'), __file__, 'exec'))" install --record /var/folders/hb/b19w4_rj14g_1736v__dgg480000gn/T/pip-hf9__sti-record/install-record.txt --single-version-externally-managed --compile:
    Building lxml version 3.4.2.

    Building without Cython.

    Using build configuration of libxslt 1.1.28

    running install

    running build

    running build_py

    creating build

    creating build/lib.macosx-10.6-intel-3.4

    creating build/lib.macosx-10.6-intel-3.4/lxml

    copying src/lxml/__init__.py -> build/lib.macosx-10.6-intel-3.4/lxml

    copying src/lxml/_elementpath.py -> build/lib.macosx-10.6-intel-3.4/lxml

    copying src/lxml/builder.py -> build/lib.macosx-10.6-intel-3.4/lxml

    copying src/lxml/cssselect.py -> build/lib.macosx-10.6-intel-3.4/lxml

    copying src/lxml/doctestcompare.py -> build/lib.macosx-10.6-intel-3.4/lxml

    copying src/lxml/ElementInclude.py -> build/lib.macosx-10.6-intel-3.4/lxml

    copying src/lxml/pyclasslookup.py -> build/lib.macosx-10.6-intel-3.4/lxml

    copying src/lxml/sax.py -> build/lib.macosx-10.6-intel-3.4/lxml

    copying src/lxml/usedoctest.py -> build/lib.macosx-10.6-intel-3.4/lxml

    creating build/lib.macosx-10.6-intel-3.4/lxml/includes

    copying src/lxml/includes/__init__.py -> build/lib.macosx-10.6-intel-3.4/lxml/includes

    creating build/lib.macosx-10.6-intel-3.4/lxml/html

    copying src/lxml/html/__init__.py -> build/lib.macosx-10.6-intel-3.4/lxml/html

    copying src/lxml/html/_diffcommand.py -> build/lib.macosx-10.6-intel-3.4/lxml/html

    copying src/lxml/html/_html5builder.py -> build/lib.macosx-10.6-intel-3.4/lxml/html

    copying src/lxml/html/_setmixin.py -> build/lib.macosx-10.6-intel-3.4/lxml/html

    copying src/lxml/html/builder.py -> build/lib.macosx-10.6-intel-3.4/lxml/html

    copying src/lxml/html/clean.py -> build/lib.macosx-10.6-intel-3.4/lxml/html

    copying src/lxml/html/defs.py -> build/lib.macosx-10.6-intel-3.4/lxml/html

    copying src/lxml/html/diff.py -> build/lib.macosx-10.6-intel-3.4/lxml/html

    copying src/lxml/html/ElementSoup.py -> build/lib.macosx-10.6-intel-3.4/lxml/html

    copying src/lxml/html/formfill.py -> build/lib.macosx-10.6-intel-3.4/lxml/html

    copying src/lxml/html/html5parser.py -> build/lib.macosx-10.6-intel-3.4/lxml/html

    copying src/lxml/html/soupparser.py -> build/lib.macosx-10.6-intel-3.4/lxml/html

    copying src/lxml/html/usedoctest.py -> build/lib.macosx-10.6-intel-3.4/lxml/html

    creating build/lib.macosx-10.6-intel-3.4/lxml/isoschematron

    copying src/lxml/isoschematron/__init__.py -> build/lib.macosx-10.6-intel-3.4/lxml/isoschematron

    copying src/lxml/lxml.etree.h -> build/lib.macosx-10.6-intel-3.4/lxml

    copying src/lxml/lxml.etree_api.h -> build/lib.macosx-10.6-intel-3.4/lxml

    copying src/lxml/includes/c14n.pxd -> build/lib.macosx-10.6-intel-3.4/lxml/includes

    copying src/lxml/includes/config.pxd -> build/lib.macosx-10.6-intel-3.4/lxml/includes

    copying src/lxml/includes/dtdvalid.pxd -> build/lib.macosx-10.6-intel-3.4/lxml/includes

    copying src/lxml/includes/etreepublic.pxd -> build/lib.macosx-10.6-intel-3.4/lxml/includes

    copying src/lxml/includes/htmlparser.pxd -> build/lib.macosx-10.6-intel-3.4/lxml/includes

    copying src/lxml/includes/relaxng.pxd -> build/lib.macosx-10.6-intel-3.4/lxml/includes

    copying src/lxml/includes/schematron.pxd -> build/lib.macosx-10.6-intel-3.4/lxml/includes

    copying src/lxml/includes/tree.pxd -> build/lib.macosx-10.6-intel-3.4/lxml/includes

    copying src/lxml/includes/uri.pxd -> build/lib.macosx-10.6-intel-3.4/lxml/includes

    copying src/lxml/includes/xinclude.pxd -> build/lib.macosx-10.6-intel-3.4/lxml/includes

    copying src/lxml/includes/xmlerror.pxd -> build/lib.macosx-10.6-intel-3.4/lxml/includes

    copying src/lxml/includes/xmlparser.pxd -> build/lib.macosx-10.6-intel-3.4/lxml/includes

    copying src/lxml/includes/xmlschema.pxd -> build/lib.macosx-10.6-intel-3.4/lxml/includes

    copying src/lxml/includes/xpath.pxd -> build/lib.macosx-10.6-intel-3.4/lxml/includes

    copying src/lxml/includes/xslt.pxd -> build/lib.macosx-10.6-intel-3.4/lxml/includes

    copying src/lxml/includes/etree_defs.h -> build/lib.macosx-10.6-intel-3.4/lxml/includes

    copying src/lxml/includes/lxml-version.h -> build/lib.macosx-10.6-intel-3.4/lxml/includes

    creating build/lib.macosx-10.6-intel-3.4/lxml/isoschematron/resources

    creating build/lib.macosx-10.6-intel-3.4/lxml/isoschematron/resources/rng

    copying src/lxml/isoschematron/resources/rng/iso-schematron.rng -> build/lib.macosx-10.6-intel-3.4/lxml/isoschematron/resources/rng

    creating build/lib.macosx-10.6-intel-3.4/lxml/isoschematron/resources/xsl

    copying src/lxml/isoschematron/resources/xsl/RNG2Schtrn.xsl -> build/lib.macosx-10.6-intel-3.4/lxml/isoschematron/resources/xsl

    copying src/lxml/isoschematron/resources/xsl/XSD2Schtrn.xsl -> build/lib.macosx-10.6-intel-3.4/lxml/isoschematron/resources/xsl

    creating build/lib.macosx-10.6-intel-3.4/lxml/isoschematron/resources/xsl/iso-schematron-xslt1

    copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/iso_abstract_expand.xsl -> build/lib.macosx-10.6-intel-3.4/lxml/isoschematron/resources/xsl/iso-schematron-xslt1

    copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/iso_dsdl_include.xsl -> build/lib.macosx-10.6-intel-3.4/lxml/isoschematron/resources/xsl/iso-schematron-xslt1

    copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/iso_schematron_message.xsl -> build/lib.macosx-10.6-intel-3.4/lxml/isoschematron/resources/xsl/iso-schematron-xslt1

    copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/iso_schematron_skeleton_for_xslt1.xsl -> build/lib.macosx-10.6-intel-3.4/lxml/isoschematron/resources/xsl/iso-schematron-xslt1

    copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/iso_svrl_for_xslt1.xsl -> build/lib.macosx-10.6-intel-3.4/lxml/isoschematron/resources/xsl/iso-schematron-xslt1

    copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/readme.txt -> build/lib.macosx-10.6-intel-3.4/lxml/isoschematron/resources/xsl/iso-schematron-xslt1

    running build_ext

    building 'lxml.etree' extension

    creating build/temp.macosx-10.6-intel-3.4

    creating build/temp.macosx-10.6-intel-3.4/src

    creating build/temp.macosx-10.6-intel-3.4/src/lxml

    /usr/bin/clang -fno-strict-aliasing -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -arch i386 -arch x86_64 -g -I/usr/include/libxml2 -I/private/var/folders/hb/b19w4_rj14g_1736v__dgg480000gn/T/pip-build-q1dh8_wz/lxml/src/lxml/includes -I/Library/Frameworks/Python.framework/Versions/3.4/include/python3.4m -c src/lxml/lxml.etree.c -o build/temp.macosx-10.6-intel-3.4/src/lxml/lxml.etree.o -w -flat_namespace

    In file included from src/lxml/lxml.etree.c:239:

    /private/var/folders/hb/b19w4_rj14g_1736v__dgg480000gn/T/pip-build-q1dh8_wz/lxml/src/lxml/includes/etree_defs.h:14:10: fatal error: 'libxml/xmlversion.h' file not found

    #include "libxml/xmlversion.h"

             ^

    1 error generated.

    /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/distutils/dist.py:260: UserWarning: Unknown distribution option: 'bugtrack_url'

      warnings.warn(msg)

    error: command '/usr/bin/clang' failed with exit status 1

    ----------------------------------------
    Command "/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4 -c "import setuptools, tokenize;__file__='/private/var/folders/hb/b19w4_rj14g_1736v__dgg480000gn/T/pip-build-q1dh8_wz/lxml/setup.py';exec(compile(getattr(tokenize, 'open', open)(__file__).read().replace('\r\n', '\n'), __file__, 'exec'))" install --record /var/folders/hb/b19w4_rj14g_1736v__dgg480000gn/T/pip-hf9__sti-record/install-record.txt --single-version-externally-managed --compile" failed with error code 1 in /private/var/folders/hb/b19w4_rj14g_1736v__dgg480000gn/T/pip-build-q1dh8_wz/lxml

    geococcyx:~ brisance$ xcode-select --install
    xcode-select: note: install requested for command line developer tools
    geococcyx:~ brisance$ pip3 install python-docx
    Collecting python-docx
      Using cached python-docx-0.8.5.tar.gz
    Collecting lxml>=2.3.2 (from python-docx)
      Using cached lxml-3.4.2.tar.gz
        Building lxml version 3.4.2.
        Building without Cython.
        Using build configuration of libxslt 1.1.28
        /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/distutils/dist.py:260: UserWarning: Unknown distribution option: 'bugtrack_url'
          warnings.warn(msg)
    Installing collected packages: lxml, python-docx
      Running setup.py install for lxml
        Building lxml version 3.4.2.
        Building without Cython.
        Using build configuration of libxslt 1.1.28
        building 'lxml.etree' extension
        /usr/bin/clang -fno-strict-aliasing -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -arch i386 -arch x86_64 -g -I/usr/include/libxml2 -I/private/var/folders/hb/b19w4_rj14g_1736v__dgg480000gn/T/pip-build-sc4is2j5/lxml/src/lxml/includes -I/Library/Frameworks/Python.framework/Versions/3.4/include/python3.4m -c src/lxml/lxml.etree.c -o build/temp.macosx-10.6-intel-3.4/src/lxml/lxml.etree.o -w -flat_namespace
        /usr/bin/clang -bundle -undefined dynamic_lookup -arch i386 -arch x86_64 -g build/temp.macosx-10.6-intel-3.4/src/lxml/lxml.etree.o -lxslt -lexslt -lxml2 -lz -lm -o build/lib.macosx-10.6-intel-3.4/lxml/etree.so
        building 'lxml.objectify' extension
        /usr/bin/clang -fno-strict-aliasing -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -arch i386 -arch x86_64 -g -I/usr/include/libxml2 -I/private/var/folders/hb/b19w4_rj14g_1736v__dgg480000gn/T/pip-build-sc4is2j5/lxml/src/lxml/includes -I/Library/Frameworks/Python.framework/Versions/3.4/include/python3.4m -c src/lxml/lxml.objectify.c -o build/temp.macosx-10.6-intel-3.4/src/lxml/lxml.objectify.o -w -flat_namespace
        /usr/bin/clang -bundle -undefined dynamic_lookup -arch i386 -arch x86_64 -g build/temp.macosx-10.6-intel-3.4/src/lxml/lxml.objectify.o -lxslt -lexslt -lxml2 -lz -lm -o build/lib.macosx-10.6-intel-3.4/lxml/objectify.so
        /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/distutils/dist.py:260: UserWarning: Unknown distribution option: 'bugtrack_url'
          warnings.warn(msg)
      Running setup.py install for python-docx
    Successfully installed lxml-3.4.2 python-docx-0.8.5
