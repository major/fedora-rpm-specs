Summary: Java bindings for BLAS
Name: jblas
Version: 1.2.5
Release: 7%{?dist}
License: BSD
URL: http://jblas.org

Source0: https://github.com/jblas-project/jblas/archive/jblas-%{version}.tar.gz
Patch0: 0001-Try-to-load-libraries-directly-on-Linux.patch
Patch1: 0001-Stop-using-javah.patch
Patch2: 0001-options-check-for-dynamic-libs-had-a-typo.patch
Patch3: 0001-javadoc-add-summaries-to-tables.patch
Patch4: 0002-Fix-path-to-stylesheet-and-overview.patch

%if 0%{?fedora} >= 33
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

BuildRequires:  javapackages-local
BuildRequires:  make
BuildRequires:  ant
BuildRequires:  gcc-gfortran
BuildRequires:  ruby-devel
BuildRequires:  java-devel
BuildRequires:  junit
BuildRequires:  %{blaslib}-devel

BuildRequires:  rubygem-RedCloth
BuildRequires:  rubygem-hitimes
BuildRequires:  rubygem-nokogiri
BuildRequires:  rubygem-redcarpet
BuildRequires:  rubygem-ffi
BuildRequires:  rubygem-posix-spawn
BuildRequires:  rubygem-fog-json
# fast-stemmer

%description
Wraps BLAS (e.g. OpenBLAS) using generated code through JNI. Allows Java
programs to use the full power of BLAS/LAPACK through a convenient
interface.

%package javadoc
Summary:        Javadocs for %{name}
Requires:       jpackage-utils
BuildArch:      noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}
rm -rf src/main/resources/lib/static

# turn off javadoc warnings, we don't care
sed -i.bak -r 's/overview=/additionalparam="-Xdoclint:none" \0/' build.xml

sed -i.bak -r 's/-SNAPSHOT//' build.xml

ln -s pom.xml %{name}.pom

%mvn_file org.jblas:jblas %{name}

# [javac] error: Source option 5 is no longer supported. Use 6 or later.
# [javac] error: Target option 1.5 is no longer supported. Use 1.6 or later.
sed -r -i 's/source="1.7"/source="11"/g; s/target="1.7"/target="11"/g; s/compiler="javac1.7"//g' build.xml

%build
libdir="$(cd "/usr/lib/$(gcc -print-multi-os-directory)"; pwd)"
export LC_ALL=C.UTF-8
export JAVA_HOME=$(java -XshowSettings:properties -version |& sed -r -n 's/.*java.home = (.*)/\1/p')
./configure --libpath="$libdir" --libs=%{blaslib} --dynamic-libs
%make_build CFLAGS="%{optflags} -fPIC"
ant minimal-jar
ln -s jblas-minimal-*.jar %{name}.jar

ant javadoc
rm -rf javadoc/src-html

%mvn_artifact %{name}.pom %{name}.jar

%install
%mvn_install -J javadoc

shopt -s globstar
install -pm755 src/main/resources/lib/dynamic/Linux/**/libjblas.so \
        -Dt %buildroot%{_libdir}/%{name}/

%files -f .mfiles
%{_libdir}/%{name}
%license COPYING AUTHORS
%doc RELEASE_NOTES

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.2.5-6
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.5-2
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Tue Jan  5 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.5-1
- Update to latest version, fix build (#1863897)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.2.4-11
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.4-7
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug  7 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.4-4
- Replace deprecated %%add_maven_depmap with %%mvn_file/%%mvn_install

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.4-1
- Update to latest version
- Clean up spec file

* Tue Nov 15 2016 Than Ngo <than@redhat.com> - 1.2.3-11
- add BR on ruby-devel → fix build failure
- add workaround to fix build failure on ppc64

* Sun Nov 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.3-10
- Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.3-6
- Fix rawhide build (#1106829).

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb 22 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.3-4
- Prune dependency on jpackage-utils and depend on java-headless (#1068201).

* Sun Sep 22 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.3-3
- Bump release for rebuild after libatlas so name bump.

* Mon Aug 05 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.3-2
- Make /usr/lib64/jblas owned.

* Tue Jul 30 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.3-1
- Initial packaging (#990627).
