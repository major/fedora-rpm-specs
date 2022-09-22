Name:           python-git-changelog
Version:        0.4.2
Release:        %autorelease
Summary:        Automatic Changelog generator using Jinja2 templates

License:        ISC
URL:            https://github.com/pawamoy/git-changelog
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        git-changelog.1

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Automatic Changelog generator using Jinja2 templates 
From git logs to change logs
This is a general software development utility.}

%description %_description

%package -n python3-git-changelog
Requires:       git-core
Summary:        %{summary}

%description -n python3-git-changelog %_description


%prep
%autosetup -n git-changelog-%{version}
sed -i 's/^Jinja2.*/Jinja2 = "*"/' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
install -m 0644 -p -D -t %{buildroot}%{_mandir}/man1 %{SOURCE1}
%pyproject_install
%pyproject_save_files git_changelog
rm -fv %{buildroot}%{python3_sitelib}/README.md
rm -fv %{buildroot}%{python3_sitelib}/pyproject.toml


%check
%pytest


%files -n python3-git-changelog -f %{pyproject_files}
%doc README.* CHANGELOG.* CODE_OF_CONDUCT.* CONTRIBUTING.* CREDITS.*
%license LICENSE*
%{_bindir}/git-changelog
%{_mandir}/man1/git-changelog.1*


%changelog
%autochangelog