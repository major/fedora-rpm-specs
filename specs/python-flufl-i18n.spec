Name:           python-flufl-i18n
Version:        5.1.0
Release:        %autorelease
Summary:        A high level API for internationalizing Python libraries and applications

License:        Apache-2.0
URL:            https://gitlab.com/warsaw/flufl.i18n
Source:         %{pypi_source flufl_i18n}
Patch:          flufl_i18n-no-covtest.diff

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
# see tool.hatch.envs.test in pyproject.toml
BuildRequires:  python3dist(sybil)


%global _description %{expand:
The `flufl.i18n` library provides a convenient API for managing translation
contexts in Python applications. It provides facilities not only for
single-context applications like command line scripts, but also more
sophisticated management of multiple-context applications such as Internet
servers.}

%description %_description

%package -n     python3-flufl-i18n
Summary:        %{summary}

%description -n python3-flufl-i18n %_description


%prep
%autosetup -p1 -n flufl_i18n-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l flufl


%check
%pyproject_check_import
%pytest -v


%files -n python3-flufl-i18n -f %{pyproject_files}
%doc README.rst docs/*.rst


%changelog
%autochangelog
