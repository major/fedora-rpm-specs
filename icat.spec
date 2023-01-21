%global repo_owner atextor
%global repo_name  icat 

Name:    icat
Version: 0.5
Release: 12%{?dist}
Summary: Output images in terminal

License: BSD
URL:     https://github.com/%{repo_owner}/%{repo_name}
Source0: %{URL}/archive/v%{version}/%{repo_name}-%{version}.tar.gz

BuildRequires: gcc imlib2-devel
BuildRequires: make

%description
Outputs an image on a 256-color or 24-bit color enabled terminal
with UTF-8 locale, such as gnome-terminal, konsole or rxvt-unicode (urxvt).

%prep
%setup -q -n %{repo_name}-%{version}
# Extract license from source code
awk '1;/\*\//{exit}' < icat.c > LICENSE

%build
%set_build_flags
%make_build

%install
install -m 755 -d %{buildroot}/%{_bindir}
install -m 755 ./icat %{buildroot}/%{_bindir}/icat

install -m 755 -d %{buildroot}/%{_mandir}/man1
install -m 755 ./icat.man %{buildroot}/%{_mandir}/man1/%{name}.1

%files
%doc CHANGELOG README.md
%license LICENSE
%{_bindir}/icat
%{_mandir}/man1/*

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 18 2018 Artur Iwicki <fedora@svgames.pl> - 0.5.3
- Add %%set_build_flags to %%build
- Use %%make_build instead of "make %%{?_smp_flags}"
- Add gcc to BuildRequires

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 02 2018 Artur Iwicki <fedora@svgames.pl> - 0.5-1
- Update to new upstream version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-5.20171026.git.74b4a1b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Artur Iwicki <fedora@svgames.pl> - 0.4-4.20171016.git.74b4a1b
- Fix manpage being installed with a wrong filename
- Create macros to make marking the release snapshot easier

* Tue Nov 07 2017 Artur Iwicki <fedora@svgames.pl> - 0.4-3.20171016.git.74b4a1b
- Update to latest upstream snapshot
- Specify CFLAGS when calling make, instead of patching the Makefile
- Add manpage to package

* Wed Oct 18 2017 Artur Iwicki <fedora@svgames.pl> - 0.4-2
- Modify Makefile to ensure debuginfo is generated

* Tue Oct 17 2017 Artur Iwicki <fedora@svgames.pl> - 0.4-1
- Initial packaging
