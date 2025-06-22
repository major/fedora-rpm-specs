Name:           python-unique-log-filter
Version:        0.1.0
Release:        %autorelease
Summary:        A log filter that removes duplicate log messages

License:        BSD-2-Clause
URL:            https://github.com/twizmwazin/unique_log_filter
Source:         https://github.com/twizmwazin/unique_log_filter/archive/v%{version}/unique_log_filter-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
A log filter that removes duplicate log messages.}

%description %_description

%package -n     python3-unique-log-filter
Summary:        %{summary}

%description -n python3-unique-log-filter %_description


%prep
%autosetup -p1 -n unique_log_filter-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L unique_log_filter


%check
%{py3_test_envvars} %{python3} test_unique_log_filter.py


%files -n python3-unique-log-filter -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
%autochangelog
