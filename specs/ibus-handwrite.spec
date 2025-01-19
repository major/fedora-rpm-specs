Name:       ibus-handwrite
Version:    3.0.0
Release:    27%{?dist}
Summary:    IBus handwrite project
License:    GPL-2.0-or-later
URL:        http://code.google.com/p/ibus-handwrite/
Source0:    https://github.com/microcai/ibus-handwrite/releases/download/3.0/%{name}-%{version}.tar.bz2
Patch0:     fixes-blink-issue.patch
Patch1:     ibus-handwrite-fixes-compile.patch

BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  gettext ibus-devel gtk3-devel
BuildRequires:  zinnia-devel
BuildRequires: make

Requires:   ibus

%description
IBus handwrite project.

%package        ja
Summary:        Japanese handwrite input method
Requires:       %{name} = %{version}-%{release}
Requires:       zinnia-tomoe-ja

%description    ja
The %{name}-ja package provide Japanese handwrite input method.

%package        zh_CN
Summary:        Simplified Chinese handwrite input method
Requires:       %{name} = %{version}-%{release}
Requires:       zinnia-tomoe-zh_CN

%description    zh_CN
The %{name}-zh_CN package provide Simplified Chinese handwrite input method.

%prep
%autosetup -p1

%build
autoconf
%configure --disable-static --enable-zinnia --with-zinnia-tomoe=%{_datadir}/zinnia/model/tomoe/
make %{?_smp_mflags}

%install
make DESTDIR=${RPM_BUILD_ROOT} install

# Register as AppStream components to be visible in the software center
#
# NOTE: It would be *awesome* if these files were maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/handwrite-jp.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="inputmethod">
  <id>handwrite-jp.xml</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>Japanese Handwriting</name>
  <summary>Japanese handwriting input method</summary>
  <description>
    <p>
      The handwriting input method is designed for entering Japanese text.
    </p>
    <p>
      Input methods are typing systems allowing users to input complex languages.
      They are necessary because these contain too many characters to simply be laid
      out on a traditional keyboard.
    </p>
  </description>
  <url type="homepage">http://code.google.com/p/ibus-handwrite/</url>
  <url type="bugtracker">https://code.google.com/p/ibus/issues/list</url>
  <url type="help">https://code.google.com/p/ibus/wiki/FAQ</url>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/handwrite-zh.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="inputmethod">
  <id>handwrite-zh.xml</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>Simplified Chinese Handwriting</name>
  <summary>Simplified Chinese handwriting input method</summary>
  <description>
    <p>
      The handwriting input method is designed for entering Simplified Chinese text.
    </p>
    <p>
      Input methods are typing systems allowing users to input complex languages.
      They are necessary because these contain too many characters to simply be laid
      out on a traditional keyboard.
    </p>
  </description>
  <url type="homepage">http://code.google.com/p/ibus-handwrite/</url>
  <url type="bugtracker">https://code.google.com/p/ibus/issues/list</url>
  <url type="help">https://code.google.com/p/ibus/wiki/FAQ</url>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_datadir}/ibus-handwrite
%{_libexecdir}/ibus-engine-handwrite

%files ja
%{_datadir}/appdata/handwrite-jp.appdata.xml
%{_datadir}/ibus/component/handwrite-jp.xml

%files zh_CN
%{_datadir}/appdata/handwrite-zh.appdata.xml
%{_datadir}/ibus/component/handwrite-zh.xml

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb  5 2024 Peng Wu <pwu@redhat.com> - 3.0.0-25
- Fix compile
- Resolves: RHBZ#2261243

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat May  6 2023 Peng Wu <pwu@redhat.com> - 3.0.0-21
- Migrate to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 26 2020 Peng Wu <pwu@redhat.com> - 3.0.0-15
- Fixes blink issue

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 01 2019 Takao Fuijwara <tfujiwar@redhat.com> - 3.0.0-12
* Add BR: gcc

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 25 2015 Richard Hughes <rhughes@redhat.com> - 3.0.0-2
- Register as AppStream components.

* Thu Aug 21 2014 Peng Wu <pwu@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 29 2014 Peng Wu <pwu@redhat.com> - 2.1.4-12
- Split ibus-handwrite for gnome software

* Tue Jun 17 2014 Peng Wu <pwu@redhat.com> - 2.1.4-11
- Fixes keyboard shortcut

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 25 2013 Peng Wu <pwu@redhat.com> - 2.1.4-8
- Fixes aarch64 build

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 23 2012  Peng Wu <pwu@redhat.com> - 2.1.4-6
- Rebuilt for pango-1.31

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 06 2012  Peng Wu <pwu@redhat.com> - 2.1.4-4
- Rebuilt for ibus-1.4.99

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.1.4-2
- Rebuild for new libpng

* Mon Aug 01 2011  Peng Wu <pwu@redhat.com> - 2.1.4-1
- Update to 2.1.4

* Wed Mar 23 2011  Peng Wu <pwu@redhat.com> - 2.1.3-1
- Update to version 2.1.3
  Remove patch ibus-handwrite-add-tooltip.patch

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 26 2010  Peng Wu <pwu@redhat.com> - 2.1.1-1
- Update to version 2.1.1
  also add ibus-handwrite-add-tooltip.patch.

* Tue Jun 01 2010  Peng Wu <pwu@redhat.com> - 2.1.0-2
- clean up spec according to review comments.

* Thu May 20 2010  Peng Wu <pwu@redhat.com> - 2.1.0-1
- Update to version 2.1.0.

* Tue Apr 27 2010  Peng Wu <pwu@redhat.com> - 2.0.1-1 
- Update to version 2.0.1. 
  also support Japanese Handwriting Recognition.

* Fri Mar 12 2010  Peng Wu <pwu@redhat.com> - 1.2.0.20100205-2
- Use textual format of model data instead of binary format file.

* Fri Mar 05 2010  Peng Wu <pwu@redhat.com> - 1.2.0.20100205-1
- The first version.
