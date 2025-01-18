%global pkg irsim-mode
%global pkgname Emacs-irsim-mode

%if %($(pkg-config emacs) ; echo $?)
%global emacs_version 21.1
%global emacs_lispdir %{_datadir}/emacs/site-lisp
%global emacs_startdir %{_datadir}/emacs/site-lisp/site-start.d
%else
%global emacs_version %(pkg-config emacs --modversion)
%global emacs_lispdir %(pkg-config emacs --variable sitepkglispdir)
%global emacs_startdir %(pkg-config emacs --variable sitestartdir)
%endif


Name:		emacs-%{pkg}
Version:	0.1
Release:	33%{?dist}
Summary:	Irsim mode for emacs

License:	MIT
URL:		http://code.google.com/p/irsim-mode/
Source0:	http://irsim-mode.googlecode.com/files/irsim-mode.el
Source1:	%{pkg}-init.el

BuildArch:	noarch
BuildRequires:	emacs emacs-el
Requires:	emacs >= %{emacs_version}
		
Obsoletes:	%{name}-el < 0.1-31
Provides:	%{name}-el = %{version}-%{release}

%description
IRSIM is a switch-level simulator for digital logic circuits.
This is an Emacs mode for editing IRSIM netlists. It provides
syntax highlighting and an extremely pleasant method of indentation.

%prep
%{__rm} -rf %{_builddir}/%{name}-%{version}
%{__mkdir} -p %{_builddir}/%{name}-%{version}
cp -p %{SOURCE0} %{_builddir}/%{name}-%{version}
cp -p %{SOURCE1} %{_builddir}/%{name}-%{version}


%build
cd %{name}-%{version}
emacs -batch -f batch-byte-compile %{pkg}.el

%install
%{__rm} -rf %{buildroot}
cd %{name}-%{version}
%{__install} -pm 755 -d %{buildroot}%{emacs_lispdir}/irsim-mode/
%{__install} -pm 755 -d %{buildroot}%{emacs_startdir}	
%{__install} -pm 644 %{pkg}.* %{buildroot}%{emacs_lispdir}/%{pkg}
%{__install} -pm 644 %{SOURCE1} %{buildroot}%{emacs_startdir}



%files
%{emacs_lispdir}/%{pkg}/*.el
%{emacs_lispdir}/%{pkg}/*.elc
%{emacs_startdir}/%{pkg}-init.el
%dir %{emacs_lispdir}/%{pkg}
%dir %{emacs_startdir}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 15 2024 Tim Landscheidt <tim@tim-landscheidt.de> - 0.1-31
- Obsolete -el subpackage (#1234530)
- Fix typo in description

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 08 2009 Arun SAG <sagarun [AT] gmail dot com> - 0.1-6
- Fixed Requires for centos

* Mon Dec 07 2009 Arun SAG <sagarun [AT] gmail dot com> - 0.1-5
- Fixed installtion failure in EL-5
- irsim-mode handles .out files

* Thu Dec 03 2009 Arun SAG <sagarun [AT] gmail dot com> - 0.1-4
- Timestamps are preserved
- Autoloads for more file types added

* Wed Dec 02 2009 Arun SAG <sagarun [AT] gmail dot com> - 0.1-3
- Description updated
- source1 updated

* Wed Dec 02 2009 Arun SAG <sagarun [AT] gmail dot com> - 0.1-2
- Reduntant globals removed
- Description updated

* Wed Dec 02 2009 Arun SAG <sagarun [AT] gmail dot com> - 0.1-1
- Initial release 0.1-1
