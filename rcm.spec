Name:		rcm
Version:	1.3.5
Release:	2%{?dist}
Summary:	Management suite for dotfiles

License:	BSD
URL:		https://github.com/thoughtbot/rcm
Source0:	https://thoughtbot.github.io/rcm/dist/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	make
BuildRequires:	python3-cram
BuildRequires:	perl

%description
A suite of tools for managing dot-files (.zshrc, .vimrc, etc.).  This suite is
useful for committing your .*rc files to a central repository to share, but it
also scales to a more complex situation such as multiple source directories
shared between computers with some host-specific or task-specific files.

%prep
%autosetup


%build
%configure
%make_build


%install
%make_install


%check
make check


%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_mandir}/man{1,5,7}/*
%{_datadir}/rcm


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Link Dupont <linkdupont@fedoraproject.org> - 1.3.5-1
- New upstream release

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 31 2020 Link Dupont <linkdupont@fedoraproject.org> - 1.3.4-1
- New upstream release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 8 2018 Link Dupont <linkdupont@fedoraproject.org> - 1.3.3-3
- Update summary

* Tue Nov 6 2018 Link Dupont <linkdupont@fedoraproject.org> - 1.3.3-2
- Tidy up files section

* Thu Nov 1 2018 Link Dupont <linkdupont@fedoraproject.org> - 1.3.3-1
- New upstream release

* Fri Jul 14 2017 Link Dupont <linkdupont@fedoraproject.org> - 1.3.1-1
- New upstream release

* Fri Jun 17 2016 Link Dupont - 1.3.0-1
- Initial package
