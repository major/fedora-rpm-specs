%global shver 4
%global maven_group_id tw.edu.ntu.csie
%global pom_file_version 3.31
%global octpkg %{name}
%global release_date 2024-08-30
%global cpp_std c++17
%global giturl https://github.com/cjlin1/libsvm

%if %{defined rhel}
%bcond java 0
%else
%ifarch %{java_arches}
%bcond java 1
%else
%bcond java 0
%endif
%endif

%bcond octave %[!0%{?rhel}]
%bcond python %[!0%{?rhel}]

Name:           libsvm
Version:        3.35
Release:        %autorelease
Summary:        A Library for Support Vector Machines

%global upver   %(tr -d . <<< %{version})

License:        BSD-3-Clause
URL:            https://www.csie.ntu.edu.tw/~cjlin/libsvm/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{upver}/%{name}-%{upver}.tar.gz
Source1:        https://www.csie.ntu.edu.tw/~cjlin/libsvm/log
Source2:        https://www.csie.ntu.edu.tw/~cjlin/papers/guide/guide.pdf
Source3:        libsvm-svm-toy-qt.desktop
Source4:        LibSVM-svm-toy-48.png
# Java interface files
Source5:        https://repo1.maven.org/maven2/tw/edu/ntu/csie/%{name}/%{pom_file_version}/%{name}-%{pom_file_version}.pom
# Octave interface files
Source6:        libsvm.INDEX
Source7:        libsvm.CITATION
Source8:        libsvm.DESCRIPTION
Patch:          %{name}.packageMain.patch
Patch:          %{name}.javaDir.patch
Patch:          %{name}.toolsDir.patch
Patch:          %{name}.svm-toy-qt5.patch

# This can be removed when F40 reaches EOL
%if %{without java}
Obsoletes:      libsvm-java < 3.25-7
%endif

%description
LIBSVM is integrated software for support vector classification (C-SVC,
nu-SVC ), regression (epsilon-SVR, nu-SVR) and distribution estimation
(one-class SVM ).  It supports multi-class classification.

%package devel
Summary:        Development files for libsvm in C, C++ and Java
BuildRequires:  gcc-c++
BuildRequires:  make
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header and object files for libsvm in C, C++ and Java.
Install this package if you want to develop programs with libsvm.

%if %{with python}
%package -n     python3-%{name}
Summary:        Python3 tools and interfaces for libsvm
BuildRequires:  python3-devel
#gnuplot is required by easy.py
Requires:       gnuplot

%description -n python3-%{name}
Python3 tools and interfaces for libsvm.  Install this package if you
want to develop programs with libsvm in Python3.
%endif

%if %{with java}
%package        java
Summary:        Java tools and interfaces for libsvm
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  maven-local
BuildArch:      noarch
Requires:       javapackages-tools
Requires:       %{name} = %{version}-%{release}

%description    java
Java tools and interfaces for libsvm.
Install this package if you want to develop
programs with libsvm in Java.

%package        javadoc
Summary:        Javadoc for libsvm
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildArch:      noarch
Requires:       %{name}-java = %{version}-%{release}

%description    javadoc
Javadoc for libsvm
%endif

%if %{with octave}
%package -n     octave-%{name}
Summary:        Octave interface to libsvm
BuildRequires:  octave-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       octave

%description -n octave-%{name}
Octave interface for libsvm.
%endif

%package        svm-toy-qt
Summary:        QT version of svm-toy (libsvm demonstration program)
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig
BuildRequires:  qt5-qtbase-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description    svm-toy-qt
svm-toy is a libsvm demonstration program which has a qt-GUI to
display the derived separating hyperplane.

%prep
%autosetup -p0 -n %{name}-%{upver}

%conf
cp -p %{SOURCE1} ChangeLog
cp -p %{SOURCE2} %{SOURCE3} .
cp -p %{SOURCE4} %{name}-svm-toy-qt-48.png

%if %{with java}
cp -p %{SOURCE5} pom.xml

# org.sonatype.oss.oss-parent is deprecated and slated for removal from Fedora
%pom_remove_parent

# Update the POM file, which is stuck on version 3.31
%pom_xpath_set '/pom:project/pom:version' %{version}

%mvn_file %{maven_group_id}:%{name} %{maven_group_id}/%{name}
%endif

# Fix line endings
sed -i.orig 's/\r//' FAQ.html
touch -r FAQ.html.orig FAQ.html
rm FAQ.html.orig

%if %{with python}
# Fix shebangs
%py3_shebang_fix tools
# Remove useless shebangs
for p in python/libsvm/{commonutil,svm,svmutil}.py; do
    sed -i.orig '1,+1d' $p
    touch -r $p.orig $p
    rm $p.orig
done
%endif

%if %{with python}
%generate_buildrequires
cd python
%pyproject_buildrequires
%endif

%build
# Build the library
make all RPM_CFLAGS='%{build_cflags}' LIBDIR='%{_libdir}' CPP_STD='%{cpp_std}'

%if %{with java}
# Build the Java interface
%mvn_artifact pom.xml java/%{name}.jar
make -C java all javadoc
%endif

%if %{with octave}
# Build the octave interface
cd matlab
octave -H -q --no-window-system --no-site-file << EOF
make
EOF
cd -
%endif

%if %{with python}
# Build the python interface
cd python
%pyproject_wheel
cd -
%endif

%install
%make_install LIBDIR='%{_libdir}' LIBSVM_VER='%{version}' CPP_STD='%{cpp_std}'
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
cp -p %{name}-svm-toy-qt-48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
mkdir -p %{buildroot}%{_datadir}/applications
cp -p %{name}-svm-toy-qt.desktop %{buildroot}%{_datadir}/applications

ln -s %{name}.so.%{shver} %{buildroot}%{_libdir}/%{name}.so

%if %{with python}
# Python
cd python
%pyproject_install
%pyproject_save_files -l libsvm
cd -
cd tools
for p in *.py; do
    install -p -m 755 $p %{buildroot}%{_bindir}/svm-$p
done
cd -
%endif

%if %{with java}
# Java
make -C java install JAVA_TARGET_DIR='%{buildroot}%{_javadir}'
mkdir -p  %{buildroot}%{_javadocdir}/%{name}
cp -p -R java/docs/* %{buildroot}%{_javadocdir}/%{name}

%mvn_install
%endif

%if %{with octave}
# Octave
# FIXME: the *.mex files are arch-specific, so they should go into octpkglibdir
# like the *.oct files do.  But octave refuses to load them from there.  It will
# only load them if they are in octpkgdir.  I don't know why.
mkdir -p %{buildroot}%{octpkgdir}/packinfo
cp -p matlab/*.mex %{buildroot}%{octpkgdir}
cp -p COPYRIGHT %{buildroot}%{octpkgdir}/packinfo/COPYING
cp -p %{SOURCE6} %{buildroot}%{octpkgdir}/packinfo/INDEX
cp -p %{SOURCE7} %{buildroot}%{octpkgdir}/packinfo/CITATION
sed 's/@VERSION@/%{version}/;s/@DATE@/%{release_date}/' %{SOURCE8} \
    > %{buildroot}%{octpkgdir}/packinfo/DESCRIPTION
cat > %{buildroot}%{octpkgdir}/packinfo/on_uninstall.m << EOF
function on_uninstall (desc)
  error ('Can not uninstall %%s installed by the redhat package manager', desc.name);
endfunction
EOF
%endif

# Desktop files
desktop-file-install --delete-original \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}-svm-toy-qt.desktop

# Rename READMEs to avoid name collisions
mv python/README python/README-Python
mv tools/README tools/README-Tools
cp -p README java/README-Java

%if %{with octave}
%post -n octave-%{name}
%octave_cmd pkg rebuild

%preun -n octave-%{name}
%octave_pkg_preun

%postun -n octave-%{name}
%octave_cmd pkg rebuild
%endif

%files
%doc COPYRIGHT FAQ.html ChangeLog guide.pdf
%{_bindir}/svm-predict
%{_bindir}/svm-scale
%{_bindir}/svm-train
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/examples
%{_libdir}/%{name}.so.4

%files devel
%doc README
%{_includedir}/%{name}/
%{_libdir}/%{name}.so

%if %{with octave}
%files -n octave-%{name}
%{octpkgdir}/
%endif

%if %{with python}
%files -n python3-%{name} -f %{pyproject_files}
%doc python/README-Python tools/README-Tools
%{_bindir}/svm-*.py
%endif

%if %{with java}
%files java -f .mfiles
%doc java/README-Java
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}/
%endif

%files svm-toy-qt
%doc README
%{_bindir}/svm-toy-qt
%{_datadir}/icons/hicolor/48x48/apps/%{name}-svm-toy-qt-48.png
%{_datadir}/applications/*%{name}-svm-toy-qt.desktop

%changelog
%autochangelog
