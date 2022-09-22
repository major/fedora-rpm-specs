%bcond_without  tests

%global         srcname         tweepy
%global         forgeurl        https://github.com/tweepy/tweepy
Version:        4.7.0
%global         tag             v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Python interface to the Twitter API

License:        MIT
URL:            %forgeurl
Source0:        %forgesource

# NOTE(mhayden): Temporary workaround until RHBZ#2067264 is fixed.
Patch0:         tweepy-allow-older-oauthlib.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
Python interface to the Twitter API.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%description -n python3-%{srcname} %{_description}

%pyproject_extras_subpkg -n python3-%{srcname} async socks


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires -r %{?with_tests:-t}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files tweepy


%if %{with tests}
%check
%tox
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc *.md examples


%changelog
%autochangelog
