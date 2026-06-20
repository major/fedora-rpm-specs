Name:		git-review
Version:	2.5.0
Release:	%autorelease
Summary:	A Git helper for integration with Gerrit

License:	Apache-2.0
URL:		https://opendev.org/opendev/git-review
# Created by:
#   $ ./get-tarball.sh %%{version}
Source:		git-review-%{version}.tar.zst

BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	pyproject-rpm-macros
BuildRequires:	sed

Requires:	git-core

%description
An extension for source control system Git that creates and manages
review requests in the patch management system Gerrit. It replaces the
rfc.sh script.


%prep
%autosetup -p1
sed -i 's/\r//' LICENSE


%generate_buildrequires
export PBR_VERSION=%{version}
%pyproject_buildrequires


%build
export PBR_VERSION=%{version}
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l git_review

install -p -m 0644 -D git-review.1 %{buildroot}%{_mandir}/man1/git-review.1


%check
# Tests require gerrit.war file to be available
%pyproject_check_import git_review -e git_review.tests -e git_review.tests.*


%files -f %{pyproject_files}
%doc README.rst
%{_bindir}/git-review
%{_mandir}/man1/git-review.1.gz
%exclude %{python3_sitelib}/git_review/tests


%changelog
%autochangelog
