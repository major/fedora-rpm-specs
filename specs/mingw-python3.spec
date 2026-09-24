%{?mingw_package_header}

# https://src.fedoraproject.org/rpms/redhat-rpm-config/pull-request/166#comment-95032
%undefine _auto_set_build_flags

%global pkgname python3
%global py_ver 3.14
%global py_ver_nodots 314
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
Version:       3.14.7
Release:       1%{?dist}
Summary:       MinGW Windows %{pkgname}

BuildArch:     noarch
License:       Python-2.0.1
URL:           https://www.python.org/
Source0:       http://www.python.org/ftp/python/%{version}/Python-%{version}%{?pre}.tar.xz

Source1:       macros.mingw32-python3
Source2:       macros.mingw64-python3
Source3:       mingw32_python3.attr
Source4:       mingw64_python3.attr


# From https://packages.msys2.org/packages/mingw-w64-x86_64-python
Patch:         0001-build-add-with-nt-threads-and-make-it-default-on-min.patch
Patch:         0002-build-Define-MS_WINDOWS-and-others-when-compiling-wi.patch
Patch:         0003-sysmodule-Implement-flags-_is_mingw-is_mingw_ucrt-an.patch
Patch:         0004-configure-add-MACHDEP-and-platform-on-MINGW.patch
Patch:         0005-build-Add-default-cross-configuration-for-MINGW.patch
Patch:         0006-configure-enable-largefile-support-by-default-for-Mi.patch
Patch:         0007-build-Add-PC-to-CPPFLAGS-and-to-SRCDIRS-on-Mingw.patch
Patch:         0008-build-add-MINGW-support-for-posixmodule.patch
Patch:         0009-exports.h-Add-support-for-MINGW.patch
Patch:         0010-configure-add-options-so-that-shared-build-is-possib.patch
Patch:         0011-build-Add-PYD_PLATFORM_TAG.patch
Patch:         0012-build-Add-dynload_win-support-for-MinGW.patch
Patch:         0013-build-Use-.pyd-extension-suffix-fix-import-lib-insta.patch
Patch:         0014-build-Configure-SOABI-and-EXT_SUFFIX-for-MINGW.patch
Patch:         0015-build-Define-MS_DLL_ID-for-sys.winver-on-MINGW.patch
Patch:         0016-build-Ignore-main-program-for-frozen-scripts-on-MING.patch
Patch:         0017-socketmodule-add-MINGW-support.patch
Patch:         0018-build-enable-winreg-msvcrt-_winapi-winsound-and-_ove.patch
Patch:         0019-sysconfig-make-_sysconfigdata.py-relocatable.patch
Patch:         0020-sysconfig-treat-MINGW-builds-as-POSIX-builds.patch
Patch:         0021-sysconfig-Change-the-get_platform-method-in-sysconfi.patch
Patch:         0022-build-semi-native-build-sysconfig.patch
Patch:         0023-ctypes-Add-support-for-stdcall-without-underscore.patch
Patch:         0024-ctypes-add-suppor-for-ctypes.pythonapi-under-MINGW.patch
Patch:         0025-ctypes-find_library-c-should-return-None-with-ucrt.patch
Patch:         0026-site-Customize-for-MINGW.patch
Patch:         0027-site-Change-user-site-packages-path-to-include-the-e.patch
Patch:         0028-python-config-output-Windows-paths-for-the-shell-var.patch
Patch:         0029-python-config-use-the-Python-variant-of-python-confi.patch
Patch:         0030-mingw-prefer-unix-sep-if-MSYSTEM-environment-variabl.patch
Patch:         0031-build-Remove-MAXPATHLEN-default.patch
Patch:         0032-build-dont-link-with-gettext.patch
Patch:         0033-use-gnu_printf-in-format.patch
Patch:         0034-build-remove-usage-of-MS_COREDLL.patch
Patch:         0035-getcompiler-expose-MINGW-toolchain-related-informati.patch
Patch:         0036-build-fix-signal-module-build.patch
Patch:         0037-build-build-winconsoleio-and-_testconsole.patch
Patch:         0038-multiprocessing-expose-sem_unlink-to-fix-multiproces.patch
Patch:         0039-build-link-win-resource-files-and-build-pythonw.patch
Patch:         0040-pycore_fileutils-add-MINGW-support.patch
Patch:         0041-configure-fix-inet_pton-check.patch
Patch:         0042-importlib-bootstrap-path-sep.patch
Patch:         0043-configure-set-MINGW-stack-reserve.patch
Patch:         0044-tests-fix-test_bytes.patch
Patch:         0045-timemodule-add-MINGW-support.patch
Patch:         0046-configure-Disable-checks-for-dlopen-dlfcn.patch
Patch:         0047-venvlauncher-Build-venvlauncher.exe-from-PC-launcher.patch
Patch:         0048-venvlauncher-try-looking-for-the-versioned-.exe-firs.patch
Patch:         0049-venvlauncher-Skip-find-python-in-Registry-for-mingw-.patch
Patch:         0050-configure-don-t-check-for-clock_-functions.patch
Patch:         0051-CI-test-the-build-and-add-some-mingw-specific-tests.patch
Patch:         0052-configure-Default-to-without-c-locale-coercion-on-Wi.patch
Patch:         0053-tests-Fix-some-failing-tests.patch
Patch:         0054-build-def-VPATH-when-compiling-Python-sysmodule.c.patch
Patch:         0055-configure-correctly-find-native-python.patch
Patch:         0056-build-Add-extra-flags-for-_bootstrap_python.patch
Patch:         0057-getpath-add-support-for-mingw.patch
Patch:         0058-build-Don-t-build-_posixsubprocess-on-Windows.patch
Patch:         0059-ssl-module-add-MINGW-support.patch
Patch:         0060-configure-Include-winsock.h-when-checking-for-netdb-.patch
Patch:         0061-configure-always-build-_multiprocessing-on-Windows.patch
Patch:         0062-configure-build-mmap-module-on-win32.patch
Patch:         0063-configure-set-BUILDEXEEXT-and-EXEEXT.patch
Patch:         0064-configure-fix-building-some-test-modules.patch
Patch:         0065-Always-convert-to-before-passing-though-pathcch-func.patch
Patch:         0066-pylifecycle.h-remove-conflicting-_Py_CheckPython3-de.patch
Patch:         0067-dynload_win-add-env-var-for-reverting-the-legacy-DLL.patch
Patch:         0068-dynload_win-Port-GetPythonImport-to-MINGW.patch
Patch:         0069-dynload_win-make-sure-to-only-use-backslashes-for-pa.patch
Patch:         0070-dynload_win-don-t-run-_Py_CheckPython3-for-MINGW-bui.patch
Patch:         0071-build-Build-and-install-libpython3.dll-stable-ABI.patch
Patch:         0072-configure-define-_DEBUG-for-a-debug-build.patch
Patch:         0073-configure-fix-multiprocessing-module.patch
Patch:         0074-build-add-MINGW-support-for-selectmodule.patch
Patch:         0075-configure-disable-various-modules-on-MINGW.patch
Patch:         0076-configure-Add-libraries-to-fix-ctypes-on-MINGW.patch
Patch:         0077-configure-Enable-_uuid-on-MINGW.patch
Patch:         0078-configure-make-incompatible-pointer-types-a-warning.patch
Patch:         0079-tests-test_makefile-normalize-path.patch
Patch:         0080-Fix-include-naming-for-cross-build.patch
Patch:         0081-Fix-format-warning.patch
Patch:         0082-Fix-pragma-warnings.patch
Patch:         0083-math-pyhash-MINGW-support.patch
Patch:         0084-tests-Fix-test-for-library-name.patch
Patch:         0085-dictobject-MINGW-support.patch
Patch:         0086-build-Fix-export-Py_GetBuildInfo-symbol.patch
Patch:         0087-build-Allow-profile-tests-failure.patch
Patch:         0088-build-add-support-for-building-C-modules.patch
Patch:         0089-build-build-fix-the-wmi-module.patch
Patch:         0090-Fix-exports-for-_suggestions-module.patch
Patch:         0091-compileall-Normalize-paths.patch
Patch:         0092-configure-enable-64-bit-time-support-for-32-bit-buil.patch
Patch:         0093-venv-also-install-the-versioned-launchers.patch
Patch:         0094-configure-set-_WIN32_WINNT-version.patch
Patch:         0095-tests-fix-sysconfig.test_get_platform.patch
Patch:         0096-pycore_time-fix-missing-timeval.patch
Patch:         0097-mmapmodule-define-DONT_USE_SEH.patch
Patch:         0098-build-Add-ABIFLAGS-to-targets-when-needed.patch
Patch:         0099-sysconfig-patch-nt-schemes-again.patch
Patch:         0100-configure-define-_PYTHREAD_NAME_MAXLEN-for-MINGW.patch
Patch:         0101-configure-allow-older-autoconf.patch
Patch:         0102-tests-allow-sys.abiflags-to-exist.patch
Patch:         0103-makesetup-make-sure-to-link-the-built-libpython.patch


BuildRequires: make
BuildRequires: automake autoconf libtool
BuildRequires: autoconf-archive
BuildRequires: python%{py_ver}-devel

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc
# Needed for correct value of CXX in _sysconfigdata.py
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-bzip2
BuildRequires: mingw32-dlfcn
BuildRequires: mingw32-expat
BuildRequires: mingw32-libffi
BuildRequires: mingw32-openssl
BuildRequires: mingw32-sqlite
BuildRequires: mingw32-tcl
BuildRequires: mingw32-tk

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc
# Needed for correct value of CXX in _sysconfigdata.py
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-bzip2
BuildRequires: mingw64-dlfcn
BuildRequires: mingw64-expat
BuildRequires: mingw64-libffi
BuildRequires: mingw64-openssl
BuildRequires: mingw64-sqlite
BuildRequires: mingw64-tcl
BuildRequires: mingw64-tk


%description
MinGW Windows %{pkgname}


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname}
Requires:      python%{py_ver}
Requires:      python%{py_ver}-devel
Requires:      python-rpm-macros
Requires:      python3-rpm-generators
Requires:      mingw32-dlfcn
Provides:      mingw32(python(abi)) = %{py_ver}

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname}.


%package -n mingw32-%{pkgname}-test
Summary:       MinGW Windows %{pkgname} - native testsuite
Requires:      mingw32-python3

%description -n mingw32-%{pkgname}-test
MinGW Windows %{pkgname} - native testsuite.


%package -n mingw32-%{pkgname}-tkinter
Summary:       MinGW Windows %{pkgname} - GUI toolkit
Requires:      mingw32-python3

%description -n mingw32-%{pkgname}-tkinter
MinGW Windows %{pkgname} - GUI toolkit.


%package -n mingw32-%{pkgname}-idle
Summary:       MinGW Windows %{pkgname} - development environment
Requires:      mingw32-python3

%description -n mingw32-%{pkgname}-idle
MinGW Windows %{pkgname} - development environment.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname}
Requires:      python%{py_ver}
Requires:      python%{py_ver}-devel
Requires:      python-rpm-macros
Requires:      python3-rpm-generators
Requires:      mingw64-dlfcn
Provides:      mingw64(python(abi)) = %{py_ver}

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname}.


%package -n mingw64-%{pkgname}-test
Summary:       MinGW Windows %{pkgname} - native testsuite
Requires:      mingw64-python3

%description -n mingw64-%{pkgname}-test
MinGW Windows %{pkgname} - native testsuite.


%package -n mingw64-%{pkgname}-tkinter
Summary:       MinGW Windows %{pkgname} - GUI toolkit
Requires:      mingw64-python3

%description -n mingw64-%{pkgname}-tkinter
MinGW Windows %{pkgname} - GUI toolkit.


%package -n mingw64-%{pkgname}-idle
Summary:       MinGW Windows %{pkgname} - development environment
Requires:      mingw64-python3

%description -n mingw64-%{pkgname}-idle
MinGW Windows %{pkgname} - development environment.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n Python-%{version}%{?pre}
autoreconf -vfi

# Ensure that we are using the system copy of various libraries rather than copies shipped in the tarball
rm -r Modules/expat


%build
export MINGW32_MAKE_ARGS="WINDRES=%{mingw32_target}-windres LD=%{mingw32_target}-ld DLLWRAP=%{mingw32_target}-dllwrap"
export MINGW64_MAKE_ARGS="WINDRES=%{mingw64_target}-windres LD=%{mingw64_target}-ld DLLWRAP=%{mingw64_target}-dllwrap"

%mingw_configure \
--with-build-python=%{_bindir}/python%{py_ver} \
--enable-shared \
--with-system-expat \
--with-system-libmpdec \
--without-ensurepip \
--with-tzpath=%{_datadir}/share/zoneinfo \
--enable-optimizations

%mingw_make_build


%install
%mingw_make_install

# Copy some useful "stuff"
install -dm755 %{buildroot}%{mingw32_py3_libdir}/Tools/{i18n,scripts}
install -dm755 %{buildroot}%{mingw64_py3_libdir}/Tools/{i18n,scripts}
install -pm755 Tools/i18n/{msgfmt,pygettext}.py %{buildroot}%{mingw32_py3_libdir}/Tools/i18n/
install -pm755 Tools/i18n/{msgfmt,pygettext}.py %{buildroot}%{mingw64_py3_libdir}/Tools/i18n/
install -pm755 Tools/scripts/{README,*py} %{buildroot}%{mingw32_py3_libdir}/Tools/scripts/
install -pm755 Tools/scripts/{README,*py} %{buildroot}%{mingw64_py3_libdir}/Tools/scripts/

# Fix permissons
find %{buildroot} -type f | xargs chmod 0644
find %{buildroot} -type f \( -name "*.dll" -o -name "*.exe" -o -name "*.pyd" \) | xargs chmod 0755

# Don't ship manpages
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}

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


%files -n mingw32-%{pkgname}
%license LICENSE
%{_bindir}/mingw32-python3
%{_rpmconfigdir}/macros.d/macros.mingw32-python3
%{_rpmconfigdir}/fileattrs/mingw32_python3.attr
%{_prefix}/%{mingw32_target}/bin/python3
%{mingw32_bindir}/idle3*
%{mingw32_bindir}/pydoc3*
%{mingw32_bindir}/python3.exe
%{mingw32_bindir}/python3-config
%{mingw32_bindir}/python%{py_ver}.exe
%{mingw32_bindir}/python%{py_ver}-config
%{mingw32_bindir}/python3w.exe
%{mingw32_bindir}/python%{py_ver}w.exe
%{mingw32_bindir}/libpython3.dll
%{mingw32_bindir}/libpython%{py_ver}.dll
%{mingw32_py3_incdir}/
%{mingw32_libdir}/libpython3.dll.a
%{mingw32_libdir}/libpython%{py_ver}.dll.a
%{mingw32_py3_libdir}/
%{mingw32_libdir}/pkgconfig/*.pc
# Part of mingw32-python3-test
%exclude %{mingw32_py3_libdir}/test
# Part of mingw32-python3-tkinter
%exclude %{mingw32_py3_libdir}/tkinter/
%exclude %{mingw32_py3_libdir}/lib-dynload/_tkinter.cp%{py_ver_nodots}-mingw_i686_msvcrt_gnu.pyd
%exclude %{mingw32_py3_libdir}/turtle.py
%exclude %{mingw32_py3_libdir}/__pycache__/turtle*
%exclude %{mingw32_py3_libdir}/turtledemo
# Part of mingw32-python3-idle
%exclude %{mingw32_bindir}/idle3
%exclude %{mingw32_bindir}/idle%{py_ver}
%exclude %{mingw32_py3_libdir}/idlelib/

%files -n mingw32-%{pkgname}-test
%{mingw32_py3_libdir}/test

%files -n mingw32-%{pkgname}-tkinter
%{mingw32_py3_libdir}/tkinter/
%{mingw32_py3_libdir}/lib-dynload/_tkinter.cp%{py_ver_nodots}-mingw_i686_msvcrt_gnu.pyd
%{mingw32_py3_libdir}/turtle.py
%{mingw32_py3_libdir}/__pycache__/turtle*
%{mingw32_py3_libdir}/turtledemo

%files -n mingw32-%{pkgname}-idle
%{mingw32_bindir}/idle3
%{mingw32_bindir}/idle%{py_ver}
%{mingw32_py3_libdir}/idlelib/

%files -n mingw64-%{pkgname}
%license LICENSE
%{_bindir}/mingw64-python3
%{_rpmconfigdir}/macros.d/macros.mingw64-python3
%{_rpmconfigdir}/fileattrs/mingw64_python3.attr
%{_prefix}/%{mingw64_target}/bin/python3
%{mingw64_bindir}/idle3*
%{mingw64_bindir}/pydoc3*
%{mingw64_bindir}/python3.exe
%{mingw64_bindir}/python3-config
%{mingw64_bindir}/python%{py_ver}.exe
%{mingw64_bindir}/python%{py_ver}-config
%{mingw64_bindir}/python3w.exe
%{mingw64_bindir}/python%{py_ver}w.exe
%{mingw64_bindir}/libpython3.dll
%{mingw64_bindir}/libpython%{py_ver}.dll
%{mingw64_py3_incdir}/
%{mingw64_libdir}/libpython3.dll.a
%{mingw64_libdir}/libpython%{py_ver}.dll.a
%{mingw64_py3_libdir}/
%{mingw64_libdir}/pkgconfig/*.pc
# Part of mingw64-python3-test
%exclude %{mingw64_py3_libdir}/test
# Part of mingw64-python3-tkinter
%exclude %{mingw64_py3_libdir}/tkinter/
%exclude %{mingw64_py3_libdir}/lib-dynload/_tkinter.cp%{py_ver_nodots}-mingw_x86_64_msvcrt_gnu.pyd
%exclude %{mingw64_py3_libdir}/turtle.py
%exclude %{mingw64_py3_libdir}/__pycache__/turtle*
%exclude %{mingw64_py3_libdir}/turtledemo
# Part of mingw64-python3-idle
%exclude %{mingw64_bindir}/idle3
%exclude %{mingw64_bindir}/idle%{py_ver}
%exclude %{mingw64_py3_libdir}/idlelib/

%files -n mingw64-%{pkgname}-test
%{mingw64_py3_libdir}/test

%files -n mingw64-%{pkgname}-tkinter
%{mingw64_py3_libdir}/tkinter/
%{mingw64_py3_libdir}/lib-dynload/_tkinter.cp%{py_ver_nodots}-mingw_x86_64_msvcrt_gnu.pyd
%{mingw64_py3_libdir}/turtle.py
%{mingw64_py3_libdir}/__pycache__/turtle*
%{mingw64_py3_libdir}/turtledemo

%files -n mingw64-%{pkgname}-idle
%{mingw64_bindir}/idle3
%{mingw64_bindir}/idle%{py_ver}
%{mingw64_py3_libdir}/idlelib/


%changelog
* Tue Sep 22 2026 Sandro Mani <manisandro@gmail.com> - 3.14.7-1
- Update to 3.14.7

* Tue Sep 22 2026 Sandro Mani <manisandro@gmail.com> - 3.14-1
- Update to 3.14

* Fri Sep 18 2026 Sandro Mani <manisandro@gmail.com> - 3.11.16-1
- Update to 3.11.16

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Sat Apr 18 2026 Sandro Mani <manisandro@gmail.com> - 3.11.15-4
- Backport fix for CVE-2026-4786

* Tue Apr 14 2026 Sandro Mani <manisandro@gmail.com> - 3.11.15-3
- Backport fixes for CVE-2026-6100, CVE-2026-3479, CVE-2026-1502

* Fri Mar 27 2026 Sandro Mani <manisandro@gmail.com> - 3.11.15-2
- Backport fixes for CVE-2026-4519, CVE-2026-3644, CVE-2026-4224

* Fri Mar 27 2026 Sandro Mani <manisandro@gmail.com> - 3.11.15-1
- Update to 3.11.15
- Backport fix for CVE-2026-2297

* Mon Feb 09 2026 Sandro Mani <manisandro@gmail.com> - 3.11.14-7
- Backport fixes for CVE-2025-11468, CVE-2026-0672, CVE-2026-0865,
  CVE-2025-15282, CVE-2026-1299

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Tue Jan 13 2026 Sandro Mani <manisandro@gmail.com> - 3.11.14-5
- Backport proposed fix for CVE-2025-13836

* Sun Dec 14 2025 Sandro Mani <manisandro@gmail.com> - 3.11.14-4
- Backport patch for CVE-2025-12084

* Sun Nov 23 2025 Sandro Mani <manisandro@gmail.com> - 3.11.14-3
- Backport fix for CVE-2025-6075

* Sun Oct 12 2025 Sandro Mani <manisandro@gmail.com> - 3.11.14-2
- Rebuild (tcl9)

* Thu Oct 09 2025 Sandro Mani <manisandro@gmail.com> - 3.11.14-1
- Update to 3.11.14

* Sun Aug 03 2025 Sandro Mani <manisandro@gmail.com> - 3.11.13-4
- Backport upstream fix for CVE-2025-8194

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jul 13 2025 Sandro Mani <manisandro@gmail.com> - 3.11.13-2
- Backport fix for CVE-2025-6069

* Sat Jun 14 2025 Sandro Mani <manisandro@gmail.com> - 3.11.13-1
- Update to 3.11.13

* Wed Apr 16 2025 Sandro Mani <manisandro@gmail.com> - 3.11.12-1
- Update to 3.11.12

* Fri Apr 04 2025 Sandro Mani <manisandro@gmail.com> - 3.11.11-5
- Add host bindir to PATH when invoking mingwXX_python3_host

* Fri Apr 04 2025 Sandro Mani <manisandro@gmail.com> - 3.11.11-4
- Add mingw-python3_pkgconfig.patch

* Sun Mar 23 2025 Sandro Mani <manisandro@gmail.com> - 3.11.11-3
- Ensure LIBPYTHON is set

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 04 2024 Sandro Mani <manisandro@gmail.com> - 3.11.11-1
- Update to 3.11.11

* Mon Nov 18 2024 Sandro Mani <manisandro@gmail.com> - 3.11.10-2
- Backport fix for CVE-2024-9287

* Sat Nov 09 2024 Sandro Mani <manisandro@gmail.com> - 3.11.10-1
- Update to 3.11.10

* Wed Aug 28 2024 Sandro Mani <manisandro@gmail.com> - 3.11.9-2
- Backport patch for CVE-2024-8088

* Mon Aug 26 2024 Sandro Mani <manisandro@gmail.com> - 3.11.9-1
- Update to 3.11.9

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 03 2024 Sandro Mani <manisandro@gmail.com> - 3.11.8-2
- Backport patch for CVE-2024-4032

* Fri Feb 16 2024 Sandro Mani <manisandro@gmail.com> - 3.11.8-1
- Update to 3.11.8
- Backport patch for CVE-2023-27043

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 08 2023 Sandro Mani <manisandro@gmail.com> - 3.11.6-1
- Update to 3.11.6

* Thu Aug 31 2023 Sandro Mani <manisandro@gmail.com> - 3.11.5-1
- Update to 3.11.5

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Sandro Mani <manisandro@gmail.com> - 3.11.4-1
- Update to 3.11.4

* Fri Apr 07 2023 Sandro Mani <manisandro@gmail.com> - 3.11.3-1
- Update to 3.11.3

* Sun Feb 12 2023 Sandro Mani <manisandro@gmail.com> - 3.11.2-1
- Update to 3.11.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 08 2022 Sandro Mani <manisandro@gmail.com> - 3.11.1-2
- Fix broken select and socket modules

* Thu Dec 08 2022 Sandro Mani <manisandro@gmail.com> - 3.11.1-1
- Update to 3.11.1

* Mon Nov 21 2022 Sandro Mani <manisandro@gmail.com> - 3.11.0-4
- Backport patch for CVE-2022-45061

* Tue Nov 01 2022 Sandro Mani <manisandro@gmail.com> - 3.11.0-3
- Enable socket and mmap modules, enable missing pieces of os and ctypes modules

* Mon Oct 31 2022 Sandro Mani <manisandro@gmail.com> - 3.11.0-2
- Fix %%mingw_python3_host macros

* Tue Oct 25 2022 Sandro Mani <manisandro@gmail.com> - 3.11.0-1
- Update to 3.11.0

* Fri Oct 21 2022 Sandro Mani <manisandro@gmail.com> - 3.11.0-0.1.rc2
- Update to 3.11.0-rc2

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
