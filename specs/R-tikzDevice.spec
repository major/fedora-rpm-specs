Name:           R-tikzDevice
Version:        %R_rpm_version 0.12.6
Release:        %autorelease
Summary:        R Graphics Output in LaTeX Format

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:  texlive-pgf
Requires:       texlive-pgf

%description
Provides a graphics output device for R that records plots in a LaTeX-friendly
format. The device transforms plotting commands issued by R functions into
LaTeX code blocks. When included in a LaTeX document, these blocks are
interpreted with the help of 'TikZ'---a graphics package for TeX and friends
written by Till Tantau. Using the 'tikzDevice', the text of R plots can contain
LaTeX commands such as mathematical formula. The device also allows arbitrary
LaTeX code to be inserted into the output stream.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
