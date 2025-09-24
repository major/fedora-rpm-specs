%global srcname animatplot

Name:           python-%{srcname}
Version:        0.4.5
Release:        %autorelease
Summary:        Making animating in Matplotlib easy

License:        MIT
URL:            https://github.com/boutproject/animatplot-ng
Source0:        https://github.com/boutproject/animatplot-ng/archive/v%{version}/animatplot-ng-v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  git-core

%description
A Python package for making interactive animated plots build on Matplotlib.


%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  pandoc
BuildRequires:  python3dist(sphinx) >= 1.5.1
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(ipykernel)
BuildRequires:  python3dist(nbsphinx)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pytest)

%description -n python3-%{srcname}
A Python package for making interactive animated plots build on Matplotlib.


%package -n     python3-%{srcname}-doc
Summary:        Documentation for python3-%{srcname}

%description -n python3-%{srcname}-doc
Documentation for python3-%{srcname}.

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup -n %{srcname}-ng-%{version} -p1 -S git



%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

pushd docs
%{__python3} -m sphinx source html
# remove the sphinx-build leftovers
rm -rf html/.{buildinfo,doctrees}
popd


%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files -l %{srcname}


%check
%pyproject_check_import

export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%{pytest}


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%files -n python3-%{srcname}-doc
%doc docs/html


%changelog
%autochangelog
