Name:           transmageddon
Version:        1.5
Release:        29%{?dist}
Summary:        Video transcoder

License:        LGPLv2+
URL:            http://www.linuxrising.org/
Source0:        http://www.linuxrising.org/files/transmageddon-%{version}.tar.xz


# Patches from upstream Merge Requests
# Python 3.9+: https://gitlab.gnome.org/Archive/transmageddon/-/merge_requests/3
Patch0:         transmageddon-3f7dd82.patch
# Gtk3: https://gitlab.gnome.org/Archive/transmageddon/-/merge_requests/4
Patch1:         transmageddon-0b36c28f.patch

BuildArch:      noarch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  python3-devel
Requires:       gstreamer1
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
Requires:       libnotify
Requires:       python3-gobject
Requires:       python(abi) = %{python3_version}
Requires:       xdg-user-dirs-gtk

%description
Transmageddon supports almost any format as its input and can generate a very
large host of output files. The goal of the application was to help people to
create the files they need to be able to play on their mobile devices and for
people not hugely experienced with multimedia to generate a multimedia file
without having to resort to command line tools with ungainly syntaxes.


%prep
%autosetup -p1


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT PYTHON=%{__python3}

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/transmageddon.desktop

%py_byte_compile %{__python3} %{buildroot}%{_datadir}/transmageddon/

%find_lang transmageddon

%files -f transmageddon.lang
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/transmageddon
%{_datadir}/appdata/transmageddon.appdata.xml
%{_datadir}/applications/transmageddon.desktop
%{_mandir}/man1/transmageddon.1*
%{_datadir}/icons/hicolor/*/apps/transmageddon.png
%{_datadir}/transmageddon/


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5-28
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 15 2021 FeRD (Frank Dana) <ferdnyc@gmail.com> - 1.5-26
- Add patches from upstream PR to run with Python 3.9+ & specify Gtk version

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5-24
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 25 2020 Kalev Lember <klember@redhat.com> - 1.5-22
- Explicitly byte-compile python files using py_byte_compile macro
- Fix FTBFS (#1865585)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-21
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5-19
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5-17
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5-16
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5-12
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5-10
- Remove obsolete scriptlets

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 17 2015 Kalev Lember <klember@redhat.com> - 1.5-4
- Fix the build with Python 3
- Use license macro for COPYING

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 04 2014 Christian F.K. Schaller <uraeus@linuxrising.org> -1.5-1
- Update to v.1.5 Mostly contains some important bugfixes

* Fri Jul 04 2014 Kalev Lember <kalevlember@gmail.com> - 1.3-1
- Update to 1.3
- Ship the appdata file

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Apr 14 2014 Kalev Lember <kalevlember@gmail.com> - 1.1-1
- Update to 1.1
- Include new hicolor theme icons and add required rpm scriptlets

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct  7 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.25-3
- Rebuild against latest gstreamer.

* Sat Oct 06 2012 Kalev Lember <kalevlember@gmail.com> - 0.25-2
- More python3 updates

* Fri Oct 05 2012 Christian Schaller <christian.schaller@gmail.com> 0.25-1
- Update spec file for move to Python3

* Mon Sep 24 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.23-2
- Rebuild against gst-1.0.0

* Sun Sep 16 2012 Christian Schaller <christian.schaller@gmail.com> - 0.23
- Update spec file for new GTK3/GStreamer 1.0 based Transmageddon
- Add dependency of python-notify

* Fri Jul 20 2012 Kalev Lember <kalevlember@gmail.com> - 0.21-2
- Remove bundled which.py and use system python-which instead (#840239)

* Fri Jul 13 2012 Kalev Lember <kalevlember@gmail.com> - 0.21-1
- Initial build
