# For test builds, should be set to 0 for release builds.
%global alpha 0

Name:           flamp
Version:        2.2.14
Release:        2%{?dist}
Summary:        Amateur Multicast Protocol - file transfer program

License:        GPL-3.0-or-later
URL:            http://www.w1hkj.com/
%if %{alpha}
Source0:        http://www.w1hkj.com/alpha/%{name}/%{name}-%{version}.tar.gz
%else
Source0:        http://www.w1hkj.com/files/%{name}/%{name}-%{version}.tar.gz
%endif

BuildRequires:  autoconf automake libtool
BuildRequires:  desktop-file-utils
BuildRequires:  gcc gcc-c++
BuildRequires:  fltk-devel >= 1.3.0
%if 0%{?fedora}
BuildRequires:  flxmlrpc-devel
%endif
BuildRequires:  libX11-devel
BuildRequires:  make


Provides:       bundled(xz)


%description
Flamp is a program for AMP or Amateur Multicast Protocol. An flamp session will
transmit one or more files with one or more iterations of the transmission.

Each file is broken into blocks, each of which has a check sum. The receiving
station saves the blocks that pass check sum. Successive transmissions will fill
in the missing blocks provided that the new blocks pass the check sum. After the
transmission sequence, the entire file is assembled and may be saved. “Fills”
may be provided by retransmitting the entire file or by the sending station only
sending the missing blocks. Start by downloading the current version of flamp
from http://www.w1hkj.com/download.html. Install the software as you would any
of the NBEMS applications.


%prep
%autosetup -p1


%build
export CXXFLAGS="-std=c++17 $RPM_OPT_FLAGS"
%configure
%make_build


%install
%make_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 16 2024 Richard Shaw <hobbes1069@gmail.com> - 2.2.14-1
- Update to 2.2.14.

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 09 2024 Richard Shaw <hobbes1069@gmail.com> - 2.2.13-1
- Update to 2.2.13.
- Convert to SPDX license.
- Add bundled provides for lzma.

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 08 2024 Richard Shaw <hobbes1069@gmail.com> - 2.2.11-1
- Update to 2.2.11.

* Mon Nov 06 2023 Richard Shaw <hobbes1069@gmail.com> - 2.2.10-1
- Update to 2.2.10.

* Thu Sep 28 2023 Richard Shaw <hobbes1069@gmail.com> - 2.2.09-1
- Update to 2.2.09.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.07-1
- Update to 2.2.07.

* Thu Aug 05 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.06-1
- Update to 2.2.06.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.05-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Jeff Law <law@redhat.com> - 2.2.05-5
- Use equality comparisons of pointers and 0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 24 2019 Richard Shaw <hobbes1069@gmail.com> - 2.2.05-1
- Update to 2.2.05.

* Sat Feb 02 2019 Richard Shaw <hobbes1069@gmail.com> - 2.2.04.-1
- Update to 2.2.04.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.03-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 21 2015 Richard Shaw <hobbes1069@gmail.com> - 2.2.03-1
- Update to latest upstream release.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Richard Shaw <hobbes1069@gmail.com> - 2.2.02-2
- Use %%license macro where appropriate.
- Update license tag to GPLv3+ which covers the combined work.

* Tue May  5 2015 Richard Shaw <hobbes1069@gmail.com> - 2.2.02-1
- Update to latest upstream release.
- Build with external xmlrpc library.

* Sun Mar 29 2015 Richard Shaw <hobbes1069@gmail.com> - 2.2.01-1
- Update to latest upstream release.

* Tue Jan 13 2015 Richard Shaw <hobbes1069@gmail.com> - 2.2.00-1
- Update to latest upstream release.

* Sat Sep  6 2014 Richard Shaw <hobbes1069@gmail.com> - 2.1.02-2
- Attempt to patch to use system lzma-sdk.

* Mon Feb  3 2014 Richard Shaw <hobbes1069@gmail.com> - 2.1.02-1
- Initial packaging.
