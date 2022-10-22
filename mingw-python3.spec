%{?mingw_package_header}

# https://src.fedoraproject.org/rpms/redhat-rpm-config/pull-request/166#comment-95032
%undefine _auto_set_build_flags

%global pkgname python3
%global py_ver 3.10
%global py_ver_nodots 310
%global mingw32_py3_libdir       %{mingw32_libdir}/python%{py_ver}
%global mingw64_py3_libdir       %{mingw64_libdir}/python%{py_ver}
%global mingw32_py3_hostlibdir   %{_prefix}/%{mingw32_target}/lib/python%{py_ver}
%global mingw64_py3_hostlibdir   %{_prefix}/%{mingw64_target}/lib/python%{py_ver}
%global mingw32_py3_incdir       %{mingw32_includedir}/python%{py_ver}
%global mingw64_py3_incdir       %{mingw64_includedir}/python%{py_ver}
%global mingw32_python3_sitearch %{mingw32_libdir}/python%{py_ver}/site-packages
%global mingw64_python3_sitearch %{mingw64_libdir}/python%{py_ver}/site-packages

# Some of the files below /usr/lib/pythonMAJOR.MINOR/test  (e.g. bad_coding.py)
# are deliberately invalid, leading to SyntaxError exceptions if they get
# byte-compiled.
%global _python_bytecompile_errors_terminate_build 0

#global pre rc2

Name:          mingw-%{pkgname}
Version:       3.10.7
Release:       3%{?dist}
Summary:       MinGW Windows %{pkgname}

BuildArch:     noarch
License:       Python
URL:           https://www.python.org/
Source0:       http://www.python.org/ftp/python/%{version}/Python-%{version}%{?pre}.tar.xz

Source1:       macros.mingw32-python3
Source2:       macros.mingw64-python3
Source3:       mingw32_python3.attr
Source4:       mingw64_python3.attr


# Add support for building with mingw
Patch1:        mingw-python3_platform-mingw.patch
# Implement setenv for PY_COERCE_C_LOCALE
Patch2:        mingw-python3_setenv.patch
# Ignore main program for frozen scripts
Patch3:        mingw-python3_frozenmain.patch
# Fix using dllhandle and winver
Patch4:        mingw-python3_dllhandle-winver.patch
# Remove gettext dependency
Patch5:        mingw-python3_gettext.patch
# Add missing include dirs and link libraries, assorted build fixes
Patch6:        mingw-python3_build.patch
# Fix misc warnings
Patch7:        mingw-python3_warnings.patch
# Link resource files and build pythonw.exe
Patch8:        mingw-python3_pythonw.patch
# Install msilib
Patch9:        mingw-python3_msilib.patch
# Use posix layout
Patch10:       mingw-python3_posix-layout.patch
# Implement PyThread_get_thread_native_id for mingw-win-pthread
Patch11:       mingw-python3_pthread_threadid.patch
# Output list of failed modules to mods_failed.txt so that we can abort the build
Patch12:       mingw-python3_mods-failed.patch
# Adapt cygwinccompiler for cross-compiling
Patch13:       mingw-python3_adapt-cygwinccompiler.patch
# Make sysconfigdata.py relocatable
Patch14:       mingw-python3_make-sysconfigdata.py-relocatable.patch
# Adapt posix build detection
Patch15:       mingw-python3_posix-build.patch
# IO_REPARSE_TAG_APPEXECLINK does not exist in mingw (yet?)
Patch16:       mingw-python3_tag_appexeclink.patch
# Enable building some modules
Patch17:       mingw-python3_enable-modules.patch
# Disable building broken / unix-only modules
Patch18:       mingw-python3_disable-modules.patch
# Fix building multiprocessing module
Patch19:       mingw-python3_module-multiprocessing.patch
# Fix building ctypes module
Patch20:       mingw-python3_module-ctypes.patch
# Fix linking against tcl/tk
Patch21 :      mingw-python3_module-tkinter.patch
# Build winreg module
Patch22:       mingw-python3_module-winreg.patch
# Configure system calls in posixmodule
Patch23:       mingw-python3_module-posix.patch
# Fix socket module build
# See also https://github.com/msys2/MINGW-packages/issues/5184
Patch24:       mingw-python3_module-socket.patch
# Fix signal module build
Patch25:       mingw-python3_module-signal.patch
# Fix select module build
Patch26:       mingw-python3_module-select.patch
# Fix ssl module build, not use enum certificates
Patch27:       mingw-python3_module-ssl.patch
# Fix building xxsubinterpreters module
Patch28:       mingw-python3_module-xxsubinterpreters.patch
# Use posix getpath
Patch29:       mingw-python3_module-getpath-posix.patch
# Add path of executable/dll to system path so that correct dependent dlls are found
Patch30:       mingw-python3_module-getpath-execprefix.patch
# Don't use MSVC localeconv struct on mingw
Patch31:       mingw-python3_lconv.patch

BuildRequires: make
BuildRequires: automake autoconf libtool
BuildRequires: autoconf-archive
BuildRequires: python%{py_ver}-devel

BuildRequires: mingw32-filesystem >= 102
BuildRequires: mingw32-gcc
# Needed for correct value of CXX in _sysconfigdata.py
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-bzip2
BuildRequires: mingw32-expat
BuildRequires: mingw32-libffi
BuildRequires: mingw32-openssl
BuildRequires: mingw32-readline
BuildRequires: mingw32-sqlite
BuildRequires: mingw32-tcl
BuildRequires: mingw32-tk

BuildRequires: mingw64-filesystem >= 102
BuildRequires: mingw64-gcc
# Needed for correct value of CXX in _sysconfigdata.py
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-bzip2
BuildRequires: mingw64-expat
BuildRequires: mingw64-libffi
BuildRequires: mingw64-openssl
BuildRequires: mingw64-readline
BuildRequires: mingw64-sqlite
BuildRequires: mingw64-tcl
BuildRequires: mingw64-tk


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
Requires:      python%{py_ver}
Requires:      python%{py_ver}-devel
Requires:      python-rpm-macros
Requires:      python3-rpm-generators
Provides:      mingw32(python(abi)) = %{py_ver}

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
Requires:      python%{py_ver}
Requires:      python%{py_ver}-devel
Requires:      python-rpm-macros
Requires:      python3-rpm-generators
Provides:      mingw64(python(abi)) = %{py_ver}

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n Python-%{version}%{?pre}
autoreconf -vfi

# Ensure that we are using the system copy of various libraries rather than copies shipped in the tarball
rm -r Modules/expat
rm -r Modules/_ctypes/{darwin,libffi}*

# Just to be sure that we are using the wanted thread model
rm -f Python/thread_nt.h


%build
export MINGW32_MAKE_ARGS="WINDRES=%{mingw32_target}-windres LD=%{mingw32_target}-ld DLLWRAP=%{mingw32_target}-dllwrap"
export MINGW64_MAKE_ARGS="WINDRES=%{mingw64_target}-windres LD=%{mingw64_target}-ld DLLWRAP=%{mingw64_target}-dllwrap"

# TODO Drop --with-ensurepip again (broken with python3.9-beta4?)
MSYSTEM=MINGW %mingw_configure \
--enable-shared \
--with-system-expat \
--with-system-ffi \
--enable-loadable-sqlite-extensions \
--with-ensurepip=no

%mingw_make_build

# Abort build if not explicitly disabled modules failed to build
if [ -e build_win32/mods_failed.txt ]; then
    echo "The following modules failed to build for win32"
    cat build_win32/mods_failed.txt
fi
if [ -e build_win64/mods_failed.txt ]; then
    echo "The following modules failed to build for win64"
    cat build_win64/mods_failed.txt
fi
if [ -e build_win32/mods_failed.txt ] || [ -e build_win64/mods_failed.txt ]; then
    exit 1;
fi


%install
%mingw_make_install

# Link import library to libdir
ln -s %{mingw32_py3_libdir}/config-%{py_ver}/libpython%{py_ver}.dll.a %{buildroot}%{mingw32_libdir}/libpython%{py_ver}.dll.a
ln -s %{mingw64_py3_libdir}/config-%{py_ver}/libpython%{py_ver}.dll.a %{buildroot}%{mingw64_libdir}/libpython%{py_ver}.dll.a

# Copy some useful "stuff"
install -dm755 %{buildroot}%{mingw32_py3_libdir}/Tools/{i18n,scripts}
install -dm755 %{buildroot}%{mingw64_py3_libdir}/Tools/{i18n,scripts}
install -pm755 Tools/i18n/{msgfmt,pygettext}.py %{buildroot}%{mingw32_py3_libdir}/Tools/i18n/
install -pm755 Tools/i18n/{msgfmt,pygettext}.py %{buildroot}%{mingw64_py3_libdir}/Tools/i18n/
install -pm755 Tools/scripts/{README,*py} %{buildroot}%{mingw32_py3_libdir}/Tools/scripts/
install -pm755 Tools/scripts/{README,*py} %{buildroot}%{mingw64_py3_libdir}/Tools/scripts/

# Cleanup shebangs
find %{buildroot}%{mingw32_py3_libdir}/ -name '*.py' | xargs sed -i "s|#[ ]*![ ]*/usr/bin/env python$|#!/usr/bin/python3|"
find %{buildroot}%{mingw64_py3_libdir}/ -name '*.py' | xargs sed -i "s|#[ ]*![ ]*/usr/bin/env python$|#!/usr/bin/python3|"

# Remove references to build directory
for file in config-%{py_ver}/Makefile _sysconfigdata__win32_.py; do
    sed -i "s|%{_builddir}|/build|g" %{buildroot}%{mingw32_py3_libdir}/$file
    sed -i "s|%{_builddir}|/build|g" %{buildroot}%{mingw64_py3_libdir}/$file
done

# Fix permissons
find %{buildroot} -type f | xargs chmod 0644
find %{buildroot} -type f \( -name "*.dll" -o -name "*.exe" \) | xargs chmod 0755

# Don't ship manpages
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}

# Host site-packages skeleton
mkdir -p %{buildroot}%{mingw32_py3_hostlibdir}/site-packages
mkdir -p %{buildroot}%{mingw64_py3_hostlibdir}/site-packages

# Hackishly faked distutils/sysconfig.py
mkdir -p %{buildroot}%{mingw32_py3_hostlibdir}/distutils
mkdir -p %{buildroot}%{mingw64_py3_hostlibdir}/distutils
pushd %{buildroot}%{mingw32_libdir}/python%{py_ver}/distutils/
for file in *.py; do
    ln -s %{mingw32_libdir}/python%{py_ver}/distutils/$file %{buildroot}%{mingw32_py3_hostlibdir}/distutils/$file
done
popd
pushd %{buildroot}%{mingw64_libdir}/python%{py_ver}/distutils/
for file in *.py; do
    ln -s %{mingw64_libdir}/python%{py_ver}/distutils/$file %{buildroot}%{mingw64_py3_hostlibdir}/distutils/$file
done
popd
ln -s %{mingw32_py3_libdir}/distutils/command %{buildroot}%{mingw32_py3_hostlibdir}/distutils/command
ln -s %{mingw64_py3_libdir}/distutils/command %{buildroot}%{mingw64_py3_hostlibdir}/distutils/command
rm %{buildroot}%{mingw32_py3_hostlibdir}/distutils/sysconfig.py
rm %{buildroot}%{mingw64_py3_hostlibdir}/distutils/sysconfig.py

cat > %{buildroot}%{mingw32_py3_hostlibdir}/distutils/sysconfig.py <<EOF
import imp
import os
_sysconfig = imp.load_source('distutils.sysconfig', '%{mingw32_py3_libdir}/distutils/sysconfig.py')
from distutils.sysconfig import *
# Overwrite methods from sysconfig
if "mingw32" in os.getenv("CC"):
    get_python_inc = lambda plat_specific=0, prefix=None: "%{mingw32_py3_incdir}"
    get_python_lib = lambda plat_specific=0, standard_lib=0, prefix=None: "%{mingw32_python3_sitearch}"
else:
    get_python_inc = lambda plat_specific=0, prefix=None: "%{_includedir}/python%{py_ver}"
    get_python_lib = lambda plat_specific=0, standard_lib=0, prefix=None: "%{_libdir}/python%{py_ver}/site-packages"
EOF

cat > %{buildroot}%{mingw64_py3_hostlibdir}/distutils/sysconfig.py <<EOF
import imp
import os
_sysconfig = imp.load_source('distutils.sysconfig', '%{mingw64_py3_libdir}/distutils/sysconfig.py')
from distutils.sysconfig import *
# Overwrite methods from sysconfig
if "mingw32" in os.getenv("CC"):
    get_python_inc = lambda plat_specific=0, prefix=None: "%{mingw64_py3_incdir}"
    get_python_lib = lambda plat_specific=0, standard_lib=0, prefix=None: "%{mingw64_python3_sitearch}"
else:
    get_python_inc = lambda plat_specific=0, prefix=None: "%{_includedir}/python%{py_ver}"
    get_python_lib = lambda plat_specific=0, standard_lib=0, prefix=None: "%{_libdir}/python%{py_ver}/site-packages"
EOF


# Install macros
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/macros.d/macros.mingw32-python3
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_rpmconfigdir}/macros.d/macros.mingw64-python3
sed -i 's|@PY_VER@|%{py_ver}|g; s|@PY_VER_NODOTS@|%{py_ver_nodots}|g' \
  %{buildroot}%{_rpmconfigdir}/macros.d/macros.mingw32-python3 \
  %{buildroot}%{_rpmconfigdir}/macros.d/macros.mingw64-python3

# Install dependency generators
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_rpmconfigdir}/fileattrs/mingw32_python3.attr
install -Dpm 0644 %{SOURCE4} %{buildroot}%{_rpmconfigdir}/fileattrs/mingw64_python3.attr

# Wrappers
mkdir -p %{buildroot}%{_bindir}
ln -s %{_libexecdir}/mingw-scripts %{buildroot}%{_bindir}/mingw32-python3
ln -s %{_libexecdir}/mingw-scripts %{buildroot}%{_bindir}/mingw64-python3

mkdir -p %{buildroot}%{_prefix}/%{mingw32_target}/bin
cat > %{buildroot}%{_prefix}/%{mingw32_target}/bin/python3 <<EOF
#!/bin/sh
%{_bindir}/mingw32-python3 "\$@"
EOF
chmod +x %{buildroot}%{_prefix}/%{mingw32_target}/bin/python3

mkdir -p %{buildroot}%{_prefix}/%{mingw64_target}/bin
cat > %{buildroot}%{_prefix}/%{mingw64_target}/bin/python3 <<EOF
#!/bin/sh
%{_bindir}/mingw64-python3 "\$@"
EOF
chmod +x %{buildroot}%{_prefix}/%{mingw64_target}/bin/python3

# TODO: These cause unsatisfyable requires on msvcr71.dll
rm -f %{buildroot}%{mingw32_py3_libdir}/distutils/command/wininst-7.1.exe
rm -f %{buildroot}%{mingw64_py3_libdir}/distutils/command/wininst-7.1.exe

# Drop unversioned 2to3
rm %{buildroot}%{mingw32_bindir}/2to3
rm %{buildroot}%{mingw64_bindir}/2to3

# Drop pip stuff installed to native dirs
rm -f %{buildroot}%{_bindir}/pip*
rm -rf %{buildroot}%{_prefix}/lib/python%{py_ver}/site-packages/pip*


%files -n mingw32-%{pkgname}
%license LICENSE
%{_bindir}/mingw32-python3
%{_rpmconfigdir}/macros.d/macros.mingw32-python3
%{_rpmconfigdir}/fileattrs/mingw32_python3.attr
%{_prefix}/%{mingw32_target}/bin/python3
%{mingw32_py3_hostlibdir}/
%{mingw32_bindir}/2to3-%{py_ver}
%{mingw32_bindir}/idle3*
%{mingw32_bindir}/pydoc3*
%{mingw32_bindir}/python3.exe
%{mingw32_bindir}/python3-config
%{mingw32_bindir}/python%{py_ver}.exe
%{mingw32_bindir}/python%{py_ver}-config
%{mingw32_bindir}/python%{py_ver}.exe
%{mingw32_bindir}/python%{py_ver}-config
%{mingw32_bindir}/python3w.exe
%{mingw32_bindir}/libpython%{py_ver}.dll
%{mingw32_py3_incdir}/
%{mingw32_libdir}/libpython%{py_ver}.dll.a
%{mingw32_py3_libdir}/
%{mingw32_libdir}/pkgconfig/*.pc

%files -n mingw64-%{pkgname}
%license LICENSE
%{_bindir}/mingw64-python3
%{_rpmconfigdir}/macros.d/macros.mingw64-python3
%{_rpmconfigdir}/fileattrs/mingw64_python3.attr
%{_prefix}/%{mingw64_target}/bin/python3
%{mingw64_py3_hostlibdir}/
%{mingw64_bindir}/2to3-%{py_ver}
%{mingw64_bindir}/idle3*
%{mingw64_bindir}/pydoc3*
%{mingw64_bindir}/python3.exe
%{mingw64_bindir}/python3-config
%{mingw64_bindir}/python%{py_ver}.exe
%{mingw64_bindir}/python%{py_ver}-config
%{mingw64_bindir}/python%{py_ver}.exe
%{mingw64_bindir}/python%{py_ver}-config
%{mingw64_bindir}/python3w.exe
%{mingw64_bindir}/libpython%{py_ver}.dll
%{mingw64_py3_incdir}/
%{mingw64_libdir}/libpython%{py_ver}.dll.a
%{mingw64_py3_libdir}/
%{mingw64_libdir}/pkgconfig/*.pc


%changelog
* Thu Oct 20 2022 Sandro Mani <manisandro@gmail.com> - 3.10.7-3
- Add %%mingw{32,64}_python3_hostsitearch

* Tue Sep 13 2022 Sandro Mani <manisandro@gmail.com> - 3.10.7-2
- Fix lib-dynload path computation in mingw-python3 macros

* Tue Sep 13 2022 Sandro Mani <manisandro@gmail.com> - 3.10.7-1
- Update to 3.10.7

* Thu Aug 04 2022 Sandro Mani <manisandro@gmail.com> - 3.10.6-1
- Update to 3.10.6

* Wed Aug 03 2022 Sandro Mani <manisandro@gmail.com> - 3.10.5-3
- Add host build macros

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 11 2022 Sandro Mani <manisandro@gmail.com> - 3.10.5-1
- Update to 3.10.5

* Mon Mar 28 2022 Sandro Mani <manisandro@gmail.com> - 3.10.4-1
- Update to 3.10.4

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 3.10.3-2
- Rebuild with mingw-gcc-12

* Sun Mar 20 2022 Sandro Mani <manisandro@gmail.com> - 3.10.3-1
- Update to 3.10.3

* Mon Feb 28 2022 Sandro Mani <manisandro@gmail.com> - 3.10.2-14
- Re-add wrapper scripts under mingw host bin dir

* Sun Feb 27 2022 Sandro Mani <manisandro@gmail.com> - 3.10.2-13
- Require python%%{py_ver} rather than python(abi) = %%{py_ver}

* Wed Feb 23 2022 Sandro Mani <manisandro@gmail.com> - 3.10.2-12
- Rework macros

* Thu Feb 17 2022 Sandro Mani <manisandro@gmail.com> - 3.10.2-11
- Rebuild (openssl)

* Fri Feb 11 2022 Sandro Mani <manisandro@gmail.com> - 3.10.2-10
- Override runtime_library_dir_option in distutils Mingw32Compiler to prevent
  unsupported -Wl,--enable-new-dtags getting added to ldflags

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 3.10.2-9
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 3.10.2-8
- Bump release

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 3.10.2-7
- Add missing dependency generator namespace for provides

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 3.10.2-6
- Rebuild for new python dependency generator

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 3.10.2-5
- Install dependency generators

* Sat Jan 22 2022 Sandro Mani <manisandro@gmail.com> - 3.10.2-4
- Also set CFLAGS/CXX/CXXFLAGS/LDFLAGS in mingw-python wrappers

* Fri Jan 21 2022 Tom Stellard <tstellar@redhat.com> - 3.10.2-3
- Build fix for https://fedoraproject.org/wiki/Changes/SetBuildFlagsBuildCheck

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Sandro Mani <manisandro@gmail.com> - 3.10.2-1
- Update to 3.10.2

* Sun Dec 12 2021 Sandro Mani <manisandro@gmail.com> - 3.10.1-1
- Update to 3.10.1

* Tue Oct 05 2021 Sandro Mani <manisandro@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Tue Sep 14 2021 Sandro Mani <manisandro@gmail.com> - 3.10.0-0.9.rc2
- Update to 3.10.0-rc2

* Wed Aug 04 2021 Sandro Mani <manisandro@gmail.com> - 3.10.0-0.8.rc1
- Update to 3.10.0-rc1

* Fri Jul 30 2021 Sandro Mani <manisandro@gmail.com> - 3.10.0-0.7.b4
- Rebuild (libffi)

* Sat Jul 24 2021 Sandro Mani <manisandro@gmail.com> - 3.10.0-0.6.b4
- Drop _WIN32_WINNT define, mingw-9.0 defaults to _WIN32_WINNT=0xA00

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-0.5.b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Sandro Mani <manisandro@gmail.com> - 3.10.0-0.4.b4
- Update to 3.10.0-b4

* Thu Jun 24 2021 Sandro Mani <manisandro@gmail.com> - 3.10.0-0.3.b3
- Fix _POSIX_BUILD use before declaration in sysconfig

* Tue Jun 22 2021 Sandro Mani <manisandro@gmail.com> - 3.10.0-0.2.b3
- Update to 3.10.0-b3

* Thu Jun 10 2021 Sandro Mani <manisandro@gmail.com> - 3.10.0-0.1.b2
- Update to 3.10.0-b2

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.9.5-2
- Rebuilt for Python 3.10

* Wed May 05 2021 Sandro Mani <manisandro@gmail.com> - 3.9.5-1
- Update to 3.9.5

* Tue Apr 06 2021 Sandro Mani <manisandro@gmail.com> - 3.9.4-1
- Update to 3.9.4

* Sun Apr 04 2021 Sandro Mani <manisandro@gmail.com> - 3.9.3-1
- Update to 3.9.3

* Sat Feb 27 2021 Sandro Mani <manisandro@gmail.com> - 3.9.2-2
- Pass --enable-loadable-sqlite-extensions

* Mon Feb 22 2021 Sandro Mani <manisandro@gmail.com> - 3.9.2-1
- Update to 3.9.2

* Mon Feb 15 2021 Sandro Mani <manisandro@gmail.com> - 3.9.1-4
- MACHDEP=win32

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Sandro Mani <manisandro@gmail.com> - 3.9.1-2
- Backport fix for CVE-2021-3177

* Thu Dec 10 2020 Sandro Mani <manisandro@gmail.com> - 3.9.1-1
- Update to 3.9.1

* Sun Nov 08 2020 Sandro Mani <manisandro@gmail.com> - 3.9.0-4
- More mingw32,64_py3_build,install macro fixes

* Sun Nov 08 2020 Sandro Mani <manisandro@gmail.com> - 3.9.0-3
- Fix mingw32,64_py3_build macros

* Fri Nov 06 2020 Sandro Mani <manisandro@gmail.com> - 3.9.0-2
- Add %%mingw{32,64}_py3_{build,install} macros

* Tue Oct 06 2020 Sandro Mani <manisandro@gmail.com> - 3.9.0-1
- Update to 3.9.0

* Fri Sep 18 2020 Sandro Mani <manisandro@gmail.com> - 3.9.0-0.12-rc2
- Update to 3.9.0-rc2

* Wed Aug 12 2020 Sandro Mani <manisandro@gmail.com> - 3.9.0-0.11.rc1
- Update to 3.9.0-rc1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-0.10.b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Sandro Mani <manisandro@gmail.com> - 3.9.0-0.9.b5
- Update to 3.9.0-beta5

* Tue Jul 14 2020 Sandro Mani <manisandro@gmail.com> - 3.9.0-0.8.b4
- Backport patch for CVE-2019-20907

* Sun Jul 12 2020 Sandro Mani <manisandro@gmail.com> - 3.9.0-0.7.b4
- Update to 3.9.0-beta4

* Wed Jun 24 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.9.0-0.6.b3
- Add mingw32/64_python3_version_nodots

* Thu Jun 11 2020 Sandro Mani <manisandro@gmail.com> - 3.9.0-0.5.b3
- Update to 3.9.0-beta3
- Set PYTHONPLATLIBDIR=lib

* Sat May 30 2020 Sandro Mani <manisandro@gmail.com> - 3.9.0-0.2.b1
- Add mingw-python3_platlibdir.patch

* Thu May 28 2020 Sandro Mani <manisandro@gmail.com> - 3.9.0-0.1.b1
- Update to 3.9.0-beta1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.8.3-2
- Rebuilt for Python 3.9

* Sun May 17 2020 Sandro Mani <manisandro@gmail.com> - 3.8.3-1
- Update to 3.8.3

* Mon Mar 02 2020 Sandro Mani <manisandro@gmail.com> - 3.8.2-1
- Update to 3.8.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Sandro Mani <manisandro@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Wed Dec 04 2019 Sandro Mani <manisandro@gmail.com> - 3.8.0-2
- Exclude debug files

* Thu Oct 17 2019 Sandro Mani <manisandro@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 3.8.0-0.5.rc1
- Rebuild (Changes/Mingw32GccDwarf2)

* Fri Oct 04 2019 Sandro Mani <manisandro@gmail.com> - 3.8.0-0.4.rc1
- Update to 3.8.0-rc1

* Fri Sep 27 2019 Sandro Mani <manisandro@gmail.com> - 3.8.0-0.3.b4
- Remove gettext dependency
- Remove dlfcn dependency
- Update mingw-python3_adapt-cygwinccompiler.patch to ensure native gcc is not invoked

* Fri Sep 27 2019 Sandro Mani <manisandro@gmail.com> - 3.8.0-0.2.b4
- Adapt host wrappers
- Don't strip extensions

* Thu Sep 26 2019 Sandro Mani <manisandro@gmail.com> - 3.8.0-0.1.b4
- Update to 3.8.0b4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Sandro Mani <manisandro@gmail.com> - 3.7.4-1
- Update to 3.7.4

* Wed May 01 2019 Sandro Mani <manisandro@gmail.com> - 3.7.3-3
- %%define -> %%global

* Wed Apr 24 2019 Sandro Mani <manisandro@gmail.com> - 3.7.3-2
- Set _PYTHON_SYSCONFIGDATA_NAME in host wrapper

* Tue Apr 23 2019 Sandro Mani <manisandro@gmail.com> - 3.7.3-1
- Initial package
