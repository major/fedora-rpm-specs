%global srcname dirq

Name:           python-dirq
Version:        1.8
Release:        %autorelease
Summary:        Directory based queue
License:        Apache-2.0
URL:            https://github.com/cern-mig/%{name}
Source0:        http://pypi.python.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/cern-mig/python-dirq/refs/tags/v%{version}/LICENSE
Patch0:         python-dirq-no-nlink.patch
BuildArch:      noarch
BuildRequires:  python3-devel


%global _description\
The goal of this module is to offer a simple queue system using the\
underlying file system for storage, security and to prevent race\
conditions via atomic operations.  It focuses on simplicity,\
robustness and the ability to scale.\
\
The python module dirq is compatible with the Perl\
module Directory::Queue.\
robustness and the ability to scale.


%description %_description

%package -n python3-dirq
Summary:        Directory based queue

%description -n python3-dirq %_description


%prep
%setup -q -n %{srcname}-%{version}
cp -p %{SOURCE1} .
%patch -P0 -p1
find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -L dirq


%check
%{py3_test_envvars} %{python3} -m test.run_tests
rm -f test/*.pyc



%files -n python3-dirq -f  %{pyproject_files}
%license LICENSE
%doc README.rst
%doc CHANGES


%changelog
%autochangelog
