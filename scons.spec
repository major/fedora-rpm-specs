# SCons 4.* works with Python3 >= (3,5,0)
# Python2 is deprecated. 
# SCons 4 is not in EPEL8 because already provided by Centos8-stream,
# however building this package in epel8 outside official repositories is possible with Python38.
# See https://bugzilla.redhat.com/show_bug.cgi?id=1823510 

%bcond_with debug

# Package documentation files
%if 0%{?el7} || 0%{?fedora} || 0%{?eln}
%bcond_without doc
%else
%bcond_with doc
%endif

%if 0%{?el8}
%global python3_sitelib %{_prefix}/lib/python3.9/site-packages
%endif

# Install prebuilt documentation
%bcond_without prebuilt_doc

Name:      scons
Version:   4.5.2
Release:   %autorelease
Summary:   An Open Source software construction tool
License:   MIT
URL:       http://www.scons.org
Source0:   https://github.com/SCons/scons/archive/%{version}/scons-%{version}.tar.gz
Source1:   https://scons.org/doc/production/scons-doc-%{version}.tar.gz
BuildArch: noarch
BuildRequires: make

%description
SCons is an Open Source software construction tool--that is, a build
tool; an improved substitute for the classic Make utility; a better way
to build software. SCons is based on the design which won the Software
Carpentry build tool design competition in August 2000.

SCons "configuration files" are Python scripts, eliminating the need
to learn a new build tool syntax. SCons maintains a global view of
all dependencies in a tree, and can scan source (or other) files for
implicit dependencies, such as files specified on #include lines. SCons
uses MD5 signatures to rebuild only when the contents of a file have
really changed, not just when the timestamp has been touched. SCons
supports side-by-side variant builds, and is easily extended with user-
defined Builder and/or Scanner objects.

%if %{with doc}
%package doc
Summary: An Open Source software construction tool
BuildArch: noarch
%if 0%{without prebuilt_doc}
BuildRequires: python3-sphinx >= 5.1.1
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: rst2pdf, fop, ghostscript
BuildRequires: python3dist(readme-renderer) 
%endif
%description doc
Scons documentation.
%endif

%package -n     python3-%{name}
Summary: An Open Source software construction tool
%if 0%{?el7} || 0%{?el9} || 0%{?fedora} || 0%{?eln}
BuildRequires: python3-devel
BuildRequires: python3-lxml
BuildRequires: python3-wheel
BuildRequires: python3-setuptools
BuildRequires: python3-psutil
BuildRequires: python3-psutil-tests
BuildRequires: lynx
%else
BuildRequires: python39-devel
BuildRequires: python39-lxml
BuildRequires: python39-wheel
BuildRequires: python39-setuptools
BuildRequires: python39-psutil
BuildRequires: lynx
Provides:      scons-python39 = 0:%{version}-%{release}
Provides:      python39-scons = 0:%{version}-%{release}
%endif
Provides:      scons = 0:%{version}-%{release}
Provides:      scons-python3 = 0:%{version}-%{release}
Provides:      SCons = 0:%{version}-%{release}
%if 0%{?el7}
Obsoletes:     python34-%{name} < 0:%{version}-%{release}
Obsoletes:     python2-%{name} < 0:%{version}-%{release}
Obsoletes:     python-%{name} < 0:%{version}-%{release}
%endif
%py_provides python3-%{name}

%description -n python3-%{name}
SCons is an Open Source software construction tool--that is, a build
tool; an improved substitute for the classic Make utility; a better way
to build software. SCons is based on the design which won the Software
Carpentry build tool design competition in August 2000.

SCons "configuration files" are Python scripts, eliminating the need
to learn a new build tool syntax. SCons maintains a global view of
all dependencies in a tree, and can scan source (or other) files for
implicit dependencies, such as files specified on #include lines. SCons
uses MD5 signatures to rebuild only when the contents of a file have
really changed, not just when the timestamp has been touched. SCons
supports side-by-side variant builds, and is easily extended with user-
defined Builder and/or Scanner objects.

%prep
%if 0%{with prebuilt_doc}
%autosetup -n %{name}-%{version} -N
%setup -n %{name}-%{version} -q -T -D -a 1
cd ..
%else
%autosetup -N -T -b 0
cd ..
%endif

# Convert to UTF-8
for file in %{name}-%{version}/src/*.txt; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done

%if 0%{?fedora} || 0%{?eln}
%py3_shebang_fix %{name}-%{version}/scripts/scons.py
%else
pathfix%{python3_version}.py -i %{__python3} -pn %{name}-%{version}/scripts/scons.py
%endif
%if 0%{?el8}
pathfix3.9.py -i %{__python3} -pn %{name}-%{version}/scripts/scons.py
%endif

# PREVENT MANPAGES REMOVING
# See https://github.com/SCons/scons/issues/3989#issuecomment-890582380
sed -i -e 's!env.AddPostAction(tgz_file, Delete(man_pages))! !g' %{name}-%{version}/SConstruct

%build
%if 0%{?el7} || 0%{?el9} || 0%{?fedora} || 0%{?eln}
%{__python3} scripts/scons.py \
%else
%{_bindir}/python3.9 scripts/scons.py \
%endif
%if %{with debug}
 --debug=explain \
%endif
%if %{without doc}
 SKIP_DOC=True
%endif

%install
export LDFLAGS="%{build_ldflags}"
export CFLAGS="%{build_cflags}"
%if 0%{?el7} || 0%{?el9} || 0%{?fedora} || 0%{?eln}
%py3_install -- --install-scripts=%{_bindir} --install-data=%{_datadir}

pushd %{buildroot}%{_bindir} 
for i in %{name}-3 %{name}-v%{version}-%{python3_version} %{name}-%{python3_version}; do
  ln -fs %{name} %{buildroot}%{_bindir}/$i
done
for i in %{name}ign-3 %{name}ign-v%{version}-%{python3_version} %{name}ign-%{python3_version}; do
  ln -fs %{name}ign %{buildroot}%{_bindir}/$i
done
for i in %{name}-configure-cache-3 %{name}-configure-cache-v%{version}-%{python3_version} %{name}-configure-cache-%{python3_version}; do
  ln -fs %{name}-configure-cache %{buildroot}%{_bindir}/$i
done
popd

%else

%{_bindir}/python3.9 setup.py install -O1 --skip-build --root %{buildroot} \
 --install-scripts=%{_bindir} \
 --install-data=%{_datadir}

pushd %{buildroot}%{_bindir} 
for i in %{name}-3 %{name}-v%{version}-3.9 %{name}-3.9; do
  ln -fs %{name} %{buildroot}%{_bindir}/$i
done
for i in %{name}ign-3 %{name}ign-v%{version}-3.9 %{name}ign-3.9; do
  ln -fs %{name}ign %{buildroot}%{_bindir}/$i
done
for i in %{name}-configure-cache-3 %{name}-configure-cache-v%{version}-3.9 %{name}-configure-cache-3.9; do
  ln -fs %{name}-configure-cache %{buildroot}%{_bindir}/$i
done
popd
%endif
 
rm -rfv %{buildroot}%{_bindir}/__pycache__

# Install manpages
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 644 build/doc/man/*.1 %{buildroot}%{_mandir}/man1/
rm -f %{buildroot}%{_datadir}/*.1

%check
%{__python3} runtest.py -P %{__python3} --passed --quit-on-failure SCons/BuilderTests.py

%files -n python3-%{name}
%doc CHANGES.txt RELEASE.*
%license LICENSE*
%{_bindir}/%{name}
%{_bindir}/%{name}ign
%{_bindir}/%{name}-configure-cache
%{_bindir}/%{name}*-3*
%{python3_sitelib}/SCons/
%{python3_sitelib}/*.egg-info/
%{_mandir}/man1/*

%if %{with doc}
%files doc
%if 0%{without prebuilt_doc}
%doc build/doc/PDF build/doc/HTML build/doc/TEXT
%else
%doc PDF HTML EPUB TEXT
%endif
%license LICENSE*
%endif

%changelog
%autochangelog
