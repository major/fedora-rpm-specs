Name:           tralics
Version:        2.15.4
Release:        15%{?dist}
Summary:        LaTeX to XML translator
License:        CeCILL
URL:            http://www-sop.inria.fr/marelle/tralics/
Source0:        ftp://ftp-sop.inria.fr/marelle/tralics/src/%{name}-src-%{version}.tar.gz

Patch0:         testkeyval.diff

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  texlive-collection-latexextra

%description
Tralics is a free software whose purpose is to convert a LaTeX document into 
an XML file. It is used since 2002 for instance to produce the INRIA's 
annual activity report.

%prep
%autosetup -p1
for f in Licence_CeCILL_V2-en.txt ChangeLog
    do
      iconv -f ISO-8859-15 -t utf-8	\
      ${f} > ${f}.conv &&               \
      touch -r ${f} ${f}.conv &&        \
      mv -f ${f}.conv ${f}
    done
sed -i 's|tralics $(OBJECTS)|tralics $(OBJECTS) $(LDFLAGS)|' src/Makefile

%build
%make_build -C src/ CPPFLAGS="%{optflags}                     \
                    -DTRALICSDIR=\\\"%{_datadir}/%{name}\\\"  \
                    -DCONFDIR=\\\"%{_sysconfdir}/%{name}\\\"" \
                    LDFLAGS="%{?__global_ldflags}"

%install
rm -frv confdir/{README,COPYING}
install -pDm755 src/%{name} %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
install -pm644 confdir/* %{buildroot}%{_datadir}/%{name}/

%check
cd Test && ./alltests

%files
%doc ChangeLog README
%license COPYING Copyright Licence_CeCILL_V2-en.txt
%{_bindir}/%{name}
%{_datadir}/%{name}/

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar  7 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@bupkis> - 2.15.4-1
- Update to latest version (#1274713)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 11 2015 Christopher Meng <rpm@cicku.me> - 2.15.3-1
- Update to 2.15.3

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.15.2-2
- Rebuilt for GCC 5 C++11 ABI change

* Fri Jan 23 2015 Christopher Meng <rpm@cicku.me> - 2.15.2-1
- Update to 2.15.2

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct 25 2013 Christopher Meng <rpm@cicku.me> - 2.15.1-3
- Pass proper flags to make.
- Fix UTF issues of docs.

* Mon Oct 07 2013 Christopher Meng <rpm@cicku.me> - 2.15.1-2
- Move files to /usr/share so it can be found by other programs.

* Mon Jul 29 2013 Christopher Meng <rpm@cicku.me> - 2.15.1-1
- Initial Package.
