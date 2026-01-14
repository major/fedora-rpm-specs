Name:           R-git2r
Version:        %R_rpm_version 0.36.2
Release:        %autorelease
Summary:        Provides Access to Git Repositories

License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  pkgconfig(libgit2) >= 0.26.0

%description
Interface to the 'libgit2' library, which is a pure C implementation of the
'Git' core methods. Provides access to 'Git' repositories to extract data
and running some basic 'Git' commands.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
