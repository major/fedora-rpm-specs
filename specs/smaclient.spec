Name:		smaclient
Version:	1.1
Release:	25%{?dist}
Summary:	Provides access to z/VM System Management functions

License:	Artistic-2.0
URL:		http://download.sinenomine.net/smaclient/
Source0:	http://download.sinenomine.net/smaclient/%{name}-%{version}
# The helper source code was extracted from upstream's script.
Source1:	smiucv.c
Source2:	%{name}.1
Source3:	smiucv.1
# Remove helper's code from the script since it's provided as a separate file
Patch0:		%{name}-%{version}-helper.patch

BuildRequires:	gcc
Requires:	coreutils util-linux vim-common

%description
smaclient is a tool which provides a line-mode interface to the z/VM System
Management API (SMAPI) for most Unix-compatible systems such as Linux.
Smaclient can exercise all the VM management interfaces to create, modify and
destroy virtual machines without ever logging into z/VM.

%prep
%setup -q -T -c
cp -p %{SOURCE0} %{name}
cp -p %{SOURCE1} .
%patch -P0 -p0


%build
# Build the SMIUCV helper
gcc $RPM_OPT_FLAGS -o smiucv smiucv.c


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -p -m755 %{name} smiucv ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m644 %{SOURCE2} %{SOURCE3} ${RPM_BUILD_ROOT}%{_mandir}/man1/



%files
%{_bindir}/*
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/smiucv.1*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Apr 20 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1-23
- convert license to SPDX

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 26 2018 Rafael Santos <rdossant@redhat.com> - 1.1-10
- Explict gcc build req.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 18 2015 Rafael Fonseca <rdossant@redhat.com> - 1.1-4
- Add manpages for smaclient and smiucv.

* Wed Aug 12 2015 Rafael Fonseca <rdossant@redhat.com> - 1.1-3
- Update runtime requirements.
- Fix generation of debuginfo pkg.

* Wed Aug 12 2015 Rafael Fonseca <rdossant@redhat.com> - 1.1-2
- Fix installation of smiucv binary
- Fix usage of flags for compilation

* Tue Aug 11 2015 Rafael Fonseca <rdossant@redhat.com> - 1.1-1
- Initial package
