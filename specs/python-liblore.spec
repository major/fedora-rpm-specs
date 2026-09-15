%global srcname liblore

Name:           python-%{srcname}
Version:        0.9.0
Release:        %autorelease
Summary:        Library for working with public-inbox
License:        GPL-2.0-or-later
URL:            https://git.kernel.org/pub/scm/utils/%{srcname}/%{srcname}.git
Source0:        https://mirrors.edge.kernel.org/pub/software/devel/%{srcname}/%{srcname}-%{version}.tar.xz
Source1:        https://mirrors.edge.kernel.org/pub/software/devel/%{srcname}/%{srcname}-%{version}.tar.sign
# https://git.kernel.org/pub/scm/utils/b4/b4.git/plain/.keys/openpgp/linuxfoundation.org/konstantin/default
Source2:        gpgkey-DE0E66E32F1FDD0902666B96E63EDCA9329DD07E.asc
Source3:        %{name}.rpmlintrc

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
A Python library for working with public-inbox servers, particularly
lore.kernel.org. It fetches email threads, parses mbox files, and provides
utilities for working with email messages from mailing list archives.}

%description %_description


%package -n	%{srcname}
Summary:        %{summary}
Provides:       python%{python3_pkgversion}-%{srcname} = %{version}-%{release}

%description -n %{srcname} %_description


%prep
xz -dc '%{SOURCE0}' | %{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data=-
%autosetup -p1 -n %{srcname}-%{version}

# Disable pyright until it's packaged.
# See https://bugzilla.redhat.com/show_bug.cgi?id=2313788
sed -Ei -e "/^ *\"?pyright/d" pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -p -g dev


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
