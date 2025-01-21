Name:           tclap
Summary:        Template-Only Command Line Argument Parser
Version:        1.2.5
Release:        8%{?dist}
License:        MIT
URL:            http://%{name}.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

Obsoletes:      tclap-devel < 1.2.0-9
Provides:       tclap-devel = %{version}-%{release}

%description
%{name} is a small, flexible library that provides a simple interface for 
defining and accessing command line arguments. It was initially inspired by
the user friendly CLAP library. The difference is that this library is
template-only, so the argument class is type independent. Type independence 
avoids identical-except-for-type objects, such as IntArg, FloatArg, and
StringArg. While the library is not strictly compliant with the GNU or
POSIX standards, it is close.

%{name} is written in ANSI C++ and is meant to be compatible with any
standards-compliant C++ compiler. The library is implemented entirely
in header files making it easy to use and distribute with other software.

%{name} is now a mature, stable, and feature rich package. It probably will not
see much further development aside from bug fixes and compatibility updates.


%package doc
Summary:        API Documentation for %{name}
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  doxygen, graphviz

%description doc
API documentation for the Template-Only Command Line Argument Parser library


%prep
%setup -q
sed -i 's/\r//' docs/style.css
rm -rf docs/html/CVS

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
# Move the pkgconfig helper file to the right location for Fedora
# when the package is noarch
mv -f %{buildroot}%{_libdir}/pkgconfig/ %{buildroot}%{_datadir}/

# move installed docs to include them in -devel package via %%doc magic
rm -rf __tmp_doc ; mkdir __tmp_doc
mv %{buildroot}%{_docdir}/%{name}/* __tmp_doc

%check
make %{?_smp_mflags} -j1 check

%files
%{_includedir}/%{name}/
%{_datadir}/pkgconfig/%{name}.pc
%doc AUTHORS COPYING README

%files doc
%doc AUTHORS COPYING README
%doc __tmp_doc/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 09 2021 Bruno Postle <bruno@postle.net> - 1.2.5-1
- Upstream stable release

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Mar 21 2021 Bruno Postle <bruno@postle.net> - 1.2.4-1
- Upstream stable release

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Bruno Postle <bruno@postle.net> - 1.2.3-1
- Upstream stable release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 29 2017 Bruno Postle <bruno@postle.net> - 1.2.2-1
- Upstream release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Dec 14 2013 Bruno Postle 1.2.1-1
- Upstream release

* Fri Dec 13 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 1.2.0-9
- Fix duplicate documentation (#1001296)
- Fix the unusual packaging (eliminate dummy base package!)
- Remove %%_isa base package dep, since this is all noarch
- Remove explicit pkgconfig dep
- Remove %%defattr

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 05 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 1.2.0-4
- The package and sub-packages are now all noarch.
- A few cosmetic improvements have also been made.

* Thu Jul 28 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 1.2.0-3
- Re-added a main package, almost empty

* Mon Jul 04 2011 Bruno Postle 1.2.0-2
- create -devel package without a base package

* Tue Mar 08 2011 Bruno Postle 1.2.0-1
- initial fedora package

