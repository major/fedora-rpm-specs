Summary: Convert to XML on the fly
Name: xmlfy
Version: 1.5.7
Release: 7%{?dist}
License: BSD
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}-src.tar.gz
URL: http://xmlfy.sourceforge.net/

BuildRequires: make
BuildRequires:  gcc
%description 
The xmlfy command is a powerful yet lightweight tool that primarily
caters for converting ASCII, UTF-8, UTF-16 or UTF-32 based output
into XML format on the fly and dealing with common issues associated
with this kind of transformation. xmlfy can be invoked from the command
line or from within a shell script to transform data quickly, easily
and reliably.

xmlfy provides many features and options to capture and encapsulate data
between XML tags for both simple and complex XML tree hierarchies. The
behavior of xmlfy is controlled by arguments and/or by specifying a
schema file providing high levels of flexibility and customization for
differing input scenarios.

With the increasing presence of object-oriented systems requiring well
structured data presentation, xmlfy allows you to convert your raw data
into XML format easily which can then be used as input for modern
object-oriented systems e.g. XML style sheets (XSLT).

%prep
%setup -q

%build
make RPM_OPT_FLAGS="%{optflags}"

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
make DESTDIR=%{buildroot} bindir=%{_bindir} mandir=%{_mandir} RPM_OPT_FLAGS="%{optflags}" install

%files
%doc README
%doc LICENSE

%{_bindir}/*
%{_mandir}/man*/*

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 24 2013 Arthur Gouros <arthurguru@users.sourceforge.net> 1.5.6-1
- point release, consult RELEASE_NOTES file for details

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild 

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 16 2011 Arthur Gouros <arthurguru@users.sourceforge.net> 1.5.5-1
- point release, consult RELEASE_NOTES file for details

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 23 2010 Arthur Gouros <arthurguru@users.sourceforge.net> 1.5.4-1
- point release, consult RELEASE_NOTES file for details

* Thu May 20 2010 Arthur Gouros <arthurguru@users.sourceforge.net> 1.5.3-1
- point release, consult RELEASE_NOTES file for details

* Thu Feb 25 2010 Arthur Gouros <arthurguru@users.sourceforge.net> 1.5.2-1
- point release, consult RELEASE_NOTES file for details

* Wed Dec 16 2009 Arthur Gouros <arthurguru@users.sourceforge.net> 1.5.1-1
- point release, consult RELEASE_NOTES file for details

* Thu Sep 24 2009 Arthur Gouros <arthurguru@users.sourceforge.net> 1.5.0-1
- normal release, consult RELEASE_NOTES file for details

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 29 2009 Arthur Gouros <arthurguru@users.sourceforge.net> 1.4.3-1
- point release, consult RELEASE_NOTES file for details

* Thu Mar 26 2009 Arthur Gouros <arthurguru@users.sourceforge.net> 1.4.2-1
- point release, consult RELEASE_NOTES file for details

* Wed Feb 25 2009 Arthur Gouros <arthurguru@users.sourceforge.net> 1.4.1-1
- point release, consult RELEASE_NOTES file for details

* Wed Feb 11 2009 Arthur Gouros <arthurguru@users.sourceforge.net> 1.4.0-1
- normal release, consult RELEASE_NOTES file for details

* Fri Dec 05 2008 Arthur Gouros <arthurguru@users.sourceforge.net> 1.3.0-1
- normal release, consult RELEASE_NOTES file for details

* Thu Sep 18 2008 Arthur Gouros <arthurguru@users.sourceforge.net> 1.2.0-1
- normal release, consult RELEASE_NOTES file for details

* Sun Jun 08 2008 Arthur Gouros <arthurguru@users.sourceforge.net> 1.1.0-1
- normal release, consult RELEASE_NOTES file for details

* Tue May 13 2008 Arthur Gouros <arthurguru@users.sourceforge.net> 1.0.0-1
- first release, consult RELEASE_NOTES file for details

