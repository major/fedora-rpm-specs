Name:          screenruler
Version:       0.96
Release:       20%{?dist}
Summary:       GNOME screen ruler
License:       GPLv2+
URL:           https://launchpad.net/screenruler/
Source0:       http://launchpad.net/screenruler/trunk/0.9.6/+download/%{name}-0.9.6.tar.gz
Source1:       %{name}.desktop
Source2:       %{name}.appdata.xml
Patch0:        screenruler-ruby19.patch
# /usr/share/screenruler/utils/addons_ruby.rb:62:in `loop': wrong number of arguments (given 0, expected 2..3) (ArgumentError)
Patch1:        screenruler-ruby25-loop.patch
BuildRequires: desktop-file-utils
Requires:      ruby
Requires:      rubygem-gtk2 rubygem-cairo rubygem-gettext
Obsoletes:     gruler < 0.85
Provides:      gruler = %{version}-%{release}

BuildArch: noarch

%description
Screenruler is a small GNOME based utility that allows you to measure objects 
on your desktop. It can be used to take both horizontal and vertical
measurement in 6 different metrics: pixels, centimeters, inches, picas, points,
and as a percentage of the ruler’s length.

%prep
%setup -q -n %{name}
%patch0 -p0 -b ruby19
%patch1 -p1 -b .ruby25

%build

%install
mkdir -p %{buildroot}

cat << EOF > screenruler
#!/bin/bash

cd %{_datadir}/%{name}
ruby ./screenruler.rb
EOF

chmod 0755 screenruler

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp -p screenruler %{buildroot}%{_bindir}/
cp -p screenruler-icon*.png %{buildroot}%{_datadir}/pixmaps/
cp -pr utils *.rb screenruler*.* *.glade %{buildroot}%{_datadir}/%{name}/
cd %{buildroot}%{_datadir}/pixmaps
ln -s ./screenruler-icon-32x32.png screenruler-icon.png

desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
 --vendor="fedora"    \
%endif
 --dir=%{buildroot}%{_datadir}/applications  \
 %{SOURCE1}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc AUTHORS
%license COPYING
%{_bindir}/screenruler
%{_datadir}/screenruler/
%{_datadir}/pixmaps/screenruler-icon*.png
%{_datadir}/applications/*.desktop
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan  5 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.96-9
- Patch to work with ruby25 for overriding loop issue

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 16 2015 Parag Nemade <pnemade AT redhat DOT com> - 0.96-4
- Add appdata file to show this application in gnome-software
- Thanks to Samuel Gyger for appdata file (rh#1192923)
- Clean the spec to follow current packaging guidelines

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 10 2013 Deji Akingunola <dakingun@gmail.com> - 0.96-1
- Update to the latest upstream release
- Patch to wirk with ruby-1.9 (Russell Harrison, BZ #831501)

* Mon Feb 25 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.90-0.5.bzr27
- Remove --vendor from desktop-file-install for F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-0.4.bzr27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-0.3.bzr27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-0.2.bzr27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 20 2011 Deji Akingunola <dakingun@gmail.com> - 0.90-0.1
- Update to 0.9 bzr snapshot

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.85-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.85-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Oct 01 2008 Deji Akingunola <dakingun@gmail.com> - 0.85-2
- Spec clean-ups from package review 

* Mon Sep 22 2008 Deji Akingunola <dakingun@gmail.com> - 0.85-1
- Follow upstream renaming to Screenruler

* Mon Jan 14 2008 Deji Akingunola <dakingun@gmail.com> - 0.8-3
- Package review update (Bugzilla #430455)

* Mon Jan 14 2008 Deji Akingunola <dakingun@gmail.com> - 0.8-2
- Explicitly require ruby
- Also require versions of ruby-libglade2 which have been fixed of bug 428781

* Mon Jan 14 2008 Deji Akingunola <dakingun@gmail.com> - 0.8-1
- Initial package
