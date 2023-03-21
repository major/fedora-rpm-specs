%global srcname towncrier

%global common_description %{expand:
Towncrier is a utility to produce useful, summarised news files for your 
project. Rather than reading the Git history as some newer tools to produce it,
or having one single file which developers all write to, towncrier reads "news 
fragments" which contain information useful to end users.}

Name:           python-%{srcname}
Version:        22.12.0
Release:        %autorelease
Summary:        Building newsfiles for your project

License:        MIT
URL:            https://github.com/hawkowl/towncrier
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
# Relax setuptools, wheel, incremental deps
Patch0:         towncrier-relax-deps.patch
# Remove test expecting towncrier in path
Patch1:         towncrier-remove-version-test.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-twisted
BuildRequires:  git-core

%description %{common_description}

%package -n     python3-%{srcname}
Summary:        %{summary}
Provides:       %{srcname} = %{version}-%{release}

%description -n python3-%{srcname} %{common_description}

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
rm -rfv $PWD/build/lib/towncrier/test/test_check.py $PWD/build/lib/towncrier/test/test_project.py
PYTHONPATH=$PWD/build/lib %{_bindir}/trial towncrier

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%{_bindir}/towncrier

%changelog
%autochangelog
