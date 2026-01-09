Name:           R-conflicted
Version:        %R_rpm_version 1.2.0
Release:        %autorelease
Summary:        An Alternative Conflict Resolution Strategy

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
R's default conflict management system gives the most recently loaded
package precedence. This can make it hard to detect conflicts, particularly
when they arise because a package update creates ambiguity that did not
previously exist. 'conflicted' takes a different approach, making every
conflict an error and forcing you to choose which function to use.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
