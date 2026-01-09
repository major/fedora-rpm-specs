Name:           R-showtextdb
Version:        %R_rpm_version 3.0
Release:        %autorelease
Summary:        Font Files for the 'showtext' Package

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{cran_url}
Source:         %{cran_source}
Patch:          0001-Load-existing-font-file.patch

BuildArch:      noarch
BuildRequires:  R-devel
BuildRequires:  wqy-microhei-fonts
Requires:       wqy-microhei-fonts

%description
Providing font files that can be used by the 'showtext' package.

%prep
%autosetup -c -p1
rm showtextdb/inst/{AUTHORS,COPYRIGHTS}

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install

# Replace fonts by system fonts (note that this cannot be done in prep because
# R CMD INSTALL copies symlink targets.)
pushd %{buildroot}%{_R_libdir}/showtextdb
    rm fonts/*
    ln -s /usr/share/fonts/wqy-microhei-fonts/wqy-microhei.ttc fonts/wqy-microhei.ttc
popd

%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
