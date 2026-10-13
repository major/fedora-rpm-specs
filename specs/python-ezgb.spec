%global srcname ezgb

Name:           python-%{srcname}
Version:        0.2.1
Release:        %autorelease
Summary:        A standalone Python library for working with git-bug repositories
License:        GPL-2.0-or-later
URL:            https://git.kernel.org/pub/scm/utils/%{srcname}/%{srcname}.git
Source0:        https://mirrors.edge.kernel.org/pub/software/devel/%{srcname}/%{srcname}-%{version}.tar.xz
Source1:        https://mirrors.edge.kernel.org/pub/software/devel/%{srcname}/%{srcname}-%{version}.tar.sign
# https://git.kernel.org/pub/scm/utils/b4/b4.git/plain/.keys/openpgp/linuxfoundation.org/konstantin/default
Source2:        gpgkey-DE0E66E32F1FDD0902666B96E63EDCA9329DD07E.asc

# Posted uptream https://lore.kernel.org/tools/20260814123104.1616487-1-mripard@kernel.org/
Patch0:         0001-ezgb-Drop-shebang-lines-from-library-modules.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# Test dependencies are in the dev dependency group, intermixed with unwanted
# linters, typecheckers, etc.; see
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters.
# Therefore, we maintain the following list of test dependencies manually.
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(typing-extensions)

%global _description %{expand:
A standalone Python library for working with git-bug repositories. It lets you
list, create, query, and update bugs that are stored as native git objects --
no external database required.}

%description %_description


%package -n	%{srcname}
Summary:        %{summary}
Provides:       python%{python3_pkgversion}-%{srcname} = %{version}-%{release}

%description -n %{srcname} %_description


%prep
xz -dc '%{SOURCE0}' | %{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data=-
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -p


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pyproject_check_import
%pytest


%files -n %{srcname} -f %{pyproject_files}


%changelog
%autochangelog
