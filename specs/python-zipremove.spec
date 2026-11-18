Name:           python-zipremove
Version:        0.10.0
Release:        %autorelease
Summary:        Extend zipfile with remove-related capabilities

License:        MIT
URL:            https://github.com/danny0838/zipremove
Source:         %{url}/archive/v%{version}/zipremove-%{version}.tar.gz

BuildSystem:    pyproject
BuildOption(install): --assert-license zipremove

BuildArch:      noarch

BuildRequires:  python3-test

%global common_description %{expand:
This package extends the native zipfile module with remove-related
capabilities. The same codebase is currently being integrated into the CPython
standard library and is scheduled to be available natively in Python 3.16. This
package serves as a backport to support these future features today.}

%description %{common_description}


%package -n python3-zipremove
Summary:        %{summary}

%description -n python3-zipremove %{common_description}


%check -a
%{py3_test_envvars} %{python3} -m unittest --verbose


%files -n python3-zipremove -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
