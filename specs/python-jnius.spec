%global modname jnius
%global srcname py%{modname}
%global sum     Dynamic access to Java classes from Python


Name:           python-%{modname}
Version:        1.7.0
Release:        %autorelease
Summary:        %{sum}

License:        MIT
URL:            https://github.com/kivy/%{srcname}

ExclusiveArch:  %{java_arches}

Source0:        %{url}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

Patch:          pyjnius-safe-setup-remove.patch


BuildRequires:  make
# avoid strict pointer checks with gcc 14, https://bugs.gentoo.org/917562
BuildRequires:  clang

BuildRequires:  python3-devel
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(pytest)

BuildRequires:  python3dist(sphinx) 
BuildRequires:  python3dist(furo)

BuildRequires:  ant-openjdk25 
BuildRequires:  java-25-devel


# https://github.com/kivy/pyjnius/issues/307
#ExcludeArch:    ppc64 s390x

%description
%{summary}.

%package     -n python3-%{srcname}
Summary:        %{sum}
Requires:       java-25-headless
Provides:       python3-%{modname} = %{version}-%{release}


%description -n python3-%{srcname}
%{summary}.

%package        doc
Summary:        Documentation files for %{srcname}
BuildArch:      noarch

%description    doc
%{summary}.


%prep
%autosetup -p1 -n %{srcname}-%{version}
%pyproject_patch_dependency Cython:drop_upper


%generate_buildrequires
%pyproject_buildrequires


%build
export CC=%{_bindir}/clang
%pyproject_wheel

make %{_smp_mflags} -C docs SPHINXBUILD='sphinx-build-3 %{_smp_mflags}' html

# build java classes for tests
# there is also Makefile, but it calls python setup.py build_ext --inplace
# together with ant, so we don't use it not to build python bits twice
ant all


%install
%pyproject_install
%pyproject_save_files jnius jnius_config
rm -f docs/build/html/.buildinfo
rm -f docs/build/html/_static/scripts/furo-extensions.js


%check
%pyproject_check_import

pushd tests
export CLASSPATH=../build/test-classes:../build/classes
export JAVA_HOME=%{_prefix}/lib/jvm/java
# skip test failing with Python 3.13.0
k='not test_hierharchy_arraylist'
# json options fail on some arches
%ifarch s390x ppc64le riscv64
  k="${k} and not jvm_options"
%endif
%pytest -k "${k}" -v
popd


%files -n python3-%{srcname} -f %{pyproject_files}
%doc *.md

%files doc
%license LICENSE
%doc docs/build/html/


%changelog
%autochangelog
