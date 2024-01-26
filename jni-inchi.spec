%global debver 1

Name:           jni-inchi
Version:        0.8
Release:        10%{?dist}
Summary:        International Chemical Identifiers for Java

License:        LGPL-3.0-or-later
URL:            http://jni-inchi.sourceforge.net/
Source0:        https://github.com/SureChEMBL/jni-inchi/archive/v%{version}-%{debver}-deb/%{name}-%{version}.tar.gz
# Generate JNI headers with "javac -h" instead of javah.  Do not use jnati,
# which we do not have in Fedora, to load the native library.
Patch0:         %{name}-native.patch
# Fix warnings about unsafe or unchecked operations
Patch1:         %{name}-unsafe.patch
# Adapt to changes in inchi 1.06
Patch2:         %{name}-inchi106.patch
# Fix javadoc problems
Patch3:         %{name}-javadoc.patch

ExclusiveArch:  %{java_arches}

BuildRequires:  gcc
BuildRequires:  inchi-devel
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)

%description
JNI-InChI enables Java software to generate IUPAC's International
Chemical Identifiers (InChIs) by making Java Native Interface (JNI) calls
to the InChI C library developed by IUPAC.  All of the features from the
InChI library are supported:

- Standard and Non-Standard InChI generation from structures with 3D, 2D,
  or no coordinates
- Structure generation (without coordinates) from InChI
- InChIKey generation
- Check InChI / InChIKey
- InChI-to-InChI conversion
- AuxInfo to InChI input
- Access to the full range of options supported by InChI
- Full support for InChI's handling of stereochemistry

JNI-InChI is a library intended for use by developers of other projects.
It does not enable users to generate InChIs from molecule file formats
such as .mol, .cml, .mol2, or SMILES strings.  If you want to do any of
these, you should take a look at the Chemistry Development Kit (CDK) or
JUMBO, both of which include InChI generation powered by JNI-InChI.  If,
however, you are a software developer and you want want to generate the
InChI for a molecule that you already hold in memory, JNI-InChI is what
you need.

%{?javadoc_package}

%prep
%autosetup -n %{name}-%{version}-%{debver}-deb -p1

# Remove prebuilt artifacts
rm -fr src/main/resources

# Remove bundled inchi library
rm -fr src/main/native/inchi-1.03

# Remove a test class that uses a very old log4j interface
rm src/main/java/net/sf/jniinchi/Main.java

# Set the library path
sed -i 's,@LIBDIR@,%{_libdir},' \
    src/main/java/net/sf/jniinchi/JniInchiWrapper.java

# Fix end of line encoding
sed -i.orig 's/\r//' README
touch -r README.orig README
rm README.orig

# Not needed for an RPM build
%pom_remove_plugin :maven-javadoc-plugin

# Workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1981486
%pom_add_dep org.apache.commons:commons-lang3:3.12.0:test

%build
# Set the build flags.  This cannot be done in %%prep.  See
# https://bugzilla.redhat.com/show_bug.cgi?id=2044028
sed -e 's|@CFLAGS@|%{build_cflags}|' \
    -e 's|@LDFLAGS@|%{build_ldflags}|' \
    -i src/main/native/Makefile

mkdir -p target/native
export LD_LIBRARY_PATH=$PWD/target/native
%mvn_build

%install
%mvn_install

# Install the shared object
mkdir -p %{buildroot}%{_libdir}/%{name}
cp -p target/native/*.so %{buildroot}%{_libdir}/%{name}

%files -f .mfiles
%doc README README.surechembl.txt
%license LICENSE-GPL.txt LICENSE-LGPL.txt NOTICE.txt
%{_libdir}/%{name}/

%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 26 2022 Jerry James <loganjerry@gmail.com> - 0.8-6
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 0.8-5
- Remove i686 support (rhbz#2104061)

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 0.8-5
- Rebuilt for java-17-openjdk as system jdk

* Fri Jan 28 2022 Jerry James <loganjerry@gmail.com> - 0.8-4
- Recover from package-notes breakage

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 29 2021 Jerry James <loganjerry@gmail.com> - 0.8-2
- Add workaround for bz 1981486

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 17 2021 Jerry James <loganjerry@gmail.com> - 0.8-1
- Initial RPM
