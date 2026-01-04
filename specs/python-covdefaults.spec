%global date    20251223
%global commit  5a0110f24c0f4f3757b3f092672b044d38eafd70
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-covdefaults
Version:        2.3.0^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        A coverage plugin to provide sensible default settings

License:        MIT
URL:            https://github.com/asottile/covdefaults
Source:         %{url}/archive/%{commit}/covdefaults-%{commit}.tar.gz

BuildSystem:    pyproject
BuildOption(prep): -n covdefaults-%{commit}
BuildOption(install): -l covdefaults

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
A coverage plugin to provide sensible default settings}

%description %_description

%package -n     python3-covdefaults
Summary:        %{summary}

%description -n python3-covdefaults %_description

%check -a
%pytest

%files -n python3-covdefaults -f %{pyproject_files}

%changelog
%autochangelog