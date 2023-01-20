Name:           DecodeIR
Version:        2.45
Release:        22%{?dist}
Summary:        Infrared remote controls decoding library

                # hifiremote/decodeir/DecodeIRCaller.java is GPLv2
                # Other files in public domain
License:        Public Domain and GPLv2+
URL:            http://sourceforge.net/p/controlremote

                # Create tarball using something like
                #   repo="svn://svn.code.sf.net/p/controlremote/code"
                #   svn export -q $repo/tags/decodeir-2.45 DecodeIR
                #   tar czf ../DecodeIR.tar.gz DecodeIR
Source0:        DecodeIR.tar.gz
Source1:        Makefile.fedora
Source2:        license-mail.txt

                # From upstream, post-release (both)
Patch1:         0001-Add-java-library-DecodeIR.patch
Patch2:         0002-Adding-a-pom.xml.patch

BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  java-sdk
BuildRequires:  maven-local
BuildRequires: make


%description
DecodeIR is a general library which can decode signals for a large number
of infrared remote controls. It can be used as a regular C library or
through a java interface. Being a JNI library, it does not support multi-arch
installations.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        javadoc
Summary:        Javadoc for %{name}
BuildArch:      noarch

%description javadoc
Javadoc API documentation for %{name}.


%prep
%setup -qn DecodeIR
%patch1 -p1
%patch2 -p1
sed -i 's/\r//'  DecodeIR.h
cp %{SOURCE1} Makefile


%build
CFLAGS="%{optflags}" make %{?_smp_mflags}
%mvn_build


%install
make    DESTDIR=%{buildroot} \
        prefix=/usr \
        libdir=%{_libdir} \
        install
cp %{SOURCE2} .
%mvn_install


%ldconfig_scriptlets


%files -f .mfiles
%dir %{_jnidir}/DecodeIR
%dir %{_datadir}/maven-poms/DecodeIR
%doc DecodeIR.html
%license  license-mail.txt

%{_libdir}/DecodeIR
%{_libdir}/libDecodeIR.so

%files devel
%{_includedir}/*

%files javadoc -f .mfiles-javadoc
%license  license-mail.txt


%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.45-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.45-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.45-20
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.45-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.45-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.45-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.45-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.45-15
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.45-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.45-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.45-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.45-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.45-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.45-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.45-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.45-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.45-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.45-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.45-4
- Rebuilt for GCC 5 C++11 ABI change

* Sat Mar 21 2015 Alec Leamas <leamas.alec@gmail.com> - 2.45-3
- Fix empty debug package (kudos: Ville Skyttä)
- Makefile.fedora cleanup.

* Fri Mar 13 2015 Alec Leamas <leamas.alec@gmail.com> - 2.45-2
- Update license
- Make javadoc package noarch
- Make the license mail %%license

* Thu Mar 05 2015 Alec Leamas <leamas.alec@gmail.com> - 2.45-1
- Initial release
