Name:           libsigrokdecode
Version:        0.5.3
Release:        25%{?dist}
Summary:        Basic API for running protocol decoders
# Combined GPLv3+ and GPLv2+
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.sigrok.org
Source0:        %{url}/download/source/%{name}/%{name}-%{version}.tar.gz
# https://github.com/sigrokproject/libsigrokdecode/commit/9b0ad5177bd692f7556a4756bdbd2da81d9c34ce
# https://github.com/sigrokproject/libsigrokdecode/commit/c4c10b89396fe21a622b8c38dd5815a496b007bf
# https://github.com/sigrokproject/libsigrokdecode/commit/a6a5e2c8b0e9ecf5d69d0c237c8e8b717b82b36f
Patch0:         %{name}-0.5.3-python3.patch
# Upstream commit 0c35c5c5845d05e5f624c99d58af992d2f004446
Patch1:         0001-srd-drop-deprecated-PyEval_InitThreads-on-Python-3.9.patch

BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  python3-devel
BuildRequires:  autoconf libtool
BuildRequires: make

%description
%{name} is a library which provides (streaming) protocol decoding
functionality for sigrok.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1

autoreconf -f

# Bytecompile script yet again wants to break our build. Retarded!
%global _python_bytecompile_errors_terminate_build 0

%build
%configure --disable-static
V=1 make %{?_smp_mflags}


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets


%files
%doc README NEWS COPYING
%{_libdir}/libsigrokdecode.so.4*
%{_datadir}/libsigrokdecode/


%files devel
%{_includedir}/libsigrokdecode/
%{_libdir}/libsigrokdecode.so
%{_libdir}/pkgconfig/libsigrokdecode.pc


%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.3-24
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.5.3-22
- Rebuilt for Python 3.13

* Fri Apr 19 2024 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.5.3-21
- Remove -doc subpackge to prevent noarch failures due to Doxygen

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.5.3-17
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5.3-14
- Rebuilt for Python 3.11

* Tue Feb 15 2022 Dan Horák <dan[at]danny.cz> - 0.5.3-13
- use upstream fixes for Python detection

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug 01 2021 mrnuke <mr.nuke.me@gmail.com> - 0.5.3-11
- Update description to not mention programming languages

* Sun Aug 01 2021 mrnuke <mr.nuke.me[at]gmail[dot]com> - 0.5.3-10
- Detect python-3.10 correctly (stupid autohell scripts)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.3-8
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Dan Horák <dan[at]danny.cz> - 0.5.3-6
- fix build with Python 3.9

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Dan Horák <dan[at]danny.cz> - 0.5.3-1
- updated to 0.5.3

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-4
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 28 2018 mrnuke <mr.nuke.me@gmail.com> - 0.5.2-1
- New and exciting libsigrokdecode 0.5.2 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-5
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 14 2017 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.5.0-1
- Update to libsigrokdecode 0.5.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 04 2017 Dan Horák <dan[at]danny.cz> - 0.4.1-1
- updated to 0.4.1

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-1
- Rebuild for Python 3.6

* Sat Feb 06 2016 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.4.0-0
- Update to libsigrokdecode 0.4.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Jul 13 2015 Dan Horák <dan[at]danny.cz> - 0.3.1-1
- updated to 0.3.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 27 2014 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.3.0-1
- Update to libsigrokdecode-0.3.0 release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
