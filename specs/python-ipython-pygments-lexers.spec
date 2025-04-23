%global pypi_name ipython-pygments-lexers

Name:           python-%{pypi_name}
Version:        1.1.1
Release:        %{autorelease}
Summary:        Defines a variety of Pygments lexers for highlighting IPython code

%global forgeurl https://github.com/ipython/ipython-pygments-lexers
%global tag %{version}
%forgemeta

License:        BSD-3-Clause
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
A Pygments plugin for IPython code & console sessions

IPython is an interactive Python shell. Among other features, it adds
some special convenience syntax, including %magics, !shell commands and
help?. This package contains lexers for these, to use with the Pygments
syntax highlighting package.}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# flit-core >= 3.11 supports PEP639 License-File
# Currenly only F43 has that available.
%if 0%{?fedora} >= 43
%pyproject_save_files -l ipython_pygments_lexers
%else
%pyproject_save_files -L ipython_pygments_lexers
%endif


%check
%pytest -v


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%if 0%{?fedora} < 43
%license LICENSE
%endif


%changelog
%autochangelog
