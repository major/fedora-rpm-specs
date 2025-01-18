Summary: Html documentation for drgeo
Name: drgeo-doc
Version: 1.6
Release: 39%{?dist}
# Automatically converted from old format: GFDL - review is highly recommended.
License: LicenseRef-Callaway-GFDL
URL: http://www.ofset.org/drgeo

Source: http://documentation.ofset.org/drgeo/drgeo-doc-%{version}.tar.gz
BuildArch: noarch
Requires:       drgeo
%description
html documentation for drgeo

%prep
%setup -q
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/drgeo/help/{fr,es,eu,it,nl}/figures/
%{__install} -m 0644 -p -D fr/*.html %{buildroot}%{_datadir}/drgeo/help/fr
%{__install} -m 0644 -p -D fr/figures/* %{buildroot}%{_datadir}/drgeo/help/fr/figures/
%{__install} -m 0644 -p -D es/*.html %{buildroot}%{_datadir}/drgeo/help/es/
%{__install} -m 0644 -p -D es/figures/* %{buildroot}%{_datadir}/drgeo/help/es/figures/
%{__install} -m 0644 -p -D eu/*.html %{buildroot}%{_datadir}/drgeo/help/eu/
#%{__install} -m 0644 -p -D eu/figures/* %{buildroot}%{_datadir}/drgeo/help/eu/figures/
%{__install} -m 0644 -p -D it/*.html %{buildroot}%{_datadir}/drgeo/help/it/
%{__install} -m 0644 -p -D it/figures/* %{buildroot}%{_datadir}/drgeo/help/it/figures/
%{__install} -m 0644 -p -D nl/*.html %{buildroot}%{_datadir}/drgeo/help/nl/
#%{__install} -m 0644 -p -D nl/figures/* %{buildroot}%{_datadir}/drgeo/help/nl/figures/

%files
%doc AUTHORS README ChangeLog COPYING
%{_datadir}/drgeo/help

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6-38
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.6-23
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jun 13 2008 Jon Stanley <jonstanley@gmail.com> - 1.6-9
- Rebuild for vendor tag cleanup, fix license tag

* Mon Aug 28 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.6-8
- Rebuild for Fedora Extras 6

* Tue Feb 14 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.6-7
- Rebuild for FC5

* Fri Feb 10 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.6-6
- Rebuild for FC5

* Wed Nov 02 2005 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.6-5
- Own of %%{_datadir}/drgeo/help

* Wed Nov 02 2005 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.6-4
- Use %%doc for AUTHORS,README,ChangeLog,COPYING

* Tue Nov 01 2005 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.6-3
- Use %%doc for AUTHORS,README,ChangeLog,COPYING

* Tue Nov 01 2005 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.6-2
- Modify mode 755 to 644
- Add AUTHORS,README,ChangeLog,COPYING

* Thu Oct 27 2005 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.6-1
- First Build
