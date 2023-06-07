Name: kernelshark
Version: 2.2.0
Release: 3%{?dist}
Epoch: 1

# As of 1.1, only kernelshark.cpp, kshark-record.cpp and examples are GPL-2.0. The rest of kernel-shark is LGPL-2.1.
# See SPDX identifier for most accurate info
License: GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1
Summary: GUI analysis for Ftrace data captured by trace-cmd

URL: https://kernelshark.org
Source0: https://git.kernel.org/pub/scm/utils/trace-cmd/kernel-shark.git/snapshot/kernel-shark-kernelshark-v%{version}.tar.gz
Source1: %{name}.appdata.xml

ExcludeArch: %{ix86} %{arm}

BuildRequires: cmake 
BuildRequires: desktop-file-utils
BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: graphviz
BuildRequires: libappstream-glib
BuildRequires: pkgconf
BuildRequires: pkgconfig(glut)
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: libtracecmd-devel
BuildRequires: libtraceevent-devel
BuildRequires: libtracefs-devel
BuildRequires: libtracecmd >= 1.3.0
BuildRequires: trace-cmd
BuildRequires: xmlto
BuildRequires: make
BuildRequires: chrpath
BuildRequires: freeglut-devel
BuildRequires: gnu-free-sans-fonts
BuildRequires: docbook-style-xsl
BuildRequires: texlive-epstopdf
BuildRequires: ghostscript
Requires: polkit
Requires: gnu-free-sans-fonts


%description
KernelShark is a front end reader of trace-cmd output. "trace-cmd
record" and "trace-cmd extract" create a trace.dat (trace-cmd.dat)
file. kernelshark can read this file and produce a graph and list
view of its data. 

%prep
%autosetup -n kernel-shark-%{name}-v%{version}

%build
cd build
cmake ..  -DCMAKE_BUILD_TYPE=Package -D_INSTALL_PREFIX=%{_prefix} -D_LIBDIR=%{_libdir} -DCMAKE_C_FLAGS_PACKAGE="%{optflags}" -DCMAKE_EXE_LINKER_FLAGS="%{build_ldflags}" -D_DOXYGEN_DOC=1
make V=1 all doc

%install
cd build
make libdir=%{_libdir} prefix=%{_prefix} V=1 DESTDIR=%{buildroot}/  install
sed -i '/Version/d' %{buildroot}/%{_datadir}/applications/kernelshark.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/kernelshark.desktop
mkdir -p %{buildroot}%{_metainfodir}/
cp %{SOURCE1} %{buildroot}%{_metainfodir}/
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

#Remove all rpath
find %{buildroot} -type f -perm 755 -name \*so\* -exec chrpath --delete {} \;
chrpath --delete %{buildroot}/%{_bindir}/kernelshark
chrpath --delete %{buildroot}/%{_bindir}/kshark-record

%files
%doc README
%{_bindir}/kernelshark
%{_bindir}/kshark-record
%{_bindir}/kshark-su-record
%dir %{_libdir}/kernelshark
%{_libdir}/kernelshark/*
%{_datadir}/applications/kernelshark.desktop
%dir %{_datadir}/icons/kernelshark
%{_datadir}/icons/kernelshark/*
%{_datadir}/polkit-1/actions/org.freedesktop.kshark-record.policy
%{_metainfodir}/%{name}.appdata.xml
%{_libdir}/libkshark-gui.so.2.2.0
%{_libdir}/libkshark-plot.so.2.2.0
%{_libdir}/libkshark.so
%{_libdir}/libkshark.so.2
%{_libdir}/libkshark.so.2.2.0
%{_libdir}/pkgconfig/libkshark.pc
%{_includedir}/%{name}

%changelog
* Mon Jun 05 2023 Zamir SUN <sztsian@gmail.com> - 1:2.2.0-3
- SPDX migration

* Fri Jun 02 2023 Zamir SUN <sztsian@gmail.com> - 1:2.2.0-2
- Add gnu-free-sans-fonts to dependency
- Fixes: RHBZ#2211613

* Tue Apr 18 2023 Zamir SUN <sztsian@gmail.com> - 1:2.2.0-1
- Update to 2.2.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 11 2022 Zamir SUN <sztsian@gmail.com> - 1:2.1.1-1
- Update to 2.1.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Apr 15 2022 Zamir SUN <sztsian@gmail.com> - 1:2.1.0-1
- Update to 2.1.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Björn Esser <besser82@fedoraproject.org> - 1:1.3-2
- Rebuild for versioned symbols in json-c

* Tue May 11 2021 Zamir SUN <sztsian@gmail.coom> - 1.3-1
- Update to 1.3

* Mon May 10 2021 Jonathan Wakely <jwakely@redhat.com> - 1:1.2-6
- Rebuilt for removed libstdc++ symbols (#1937698)

* Wed Mar 31 2021 Jonathan Wakely <jwakely@redhat.com> - 1:1.2-5
- Rebuilt for removed libstdc++ symbols (#1937698)

* Wed Mar 24 2021 Jerome Marchand <jmarchan@redhat.com> - 1.2-3
- Rebuild with external libtracefs and libtraceevent
- Misc cleanup

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 09 2021 Zamir SUN <sztsian@gmail.coom> - 1.2-2
- Bump epoch to allow updating.

* Mon Oct 12 2020 Zamir SUN <sztsian@gmail.com> - 1.2-1
- Update to 1.2
- Uses trace event plugins from old trace-cmd dir

* Thu Sep 24 2020 Zamir SUN <sztsian@gmail.com> - 1.1-1
- Package kernelshark in a standalone package with 1.1

