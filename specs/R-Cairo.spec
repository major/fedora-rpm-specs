Name:           R-Cairo
Version:        %R_rpm_version 1.7-0
Release:        %autorelease
Summary:        Use Cairo for high-quality bitmap, vector, and display output

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:  cairo-devel >= 1.2
BuildRequires:  libXt-devel

%description
R graphics device using cairographics library that can be used to create
high-quality vector (PDF, PostScript and SVG) and bitmap output (PNG, JPEG,
TIFF), and high-quality rendering in displays (X11 and Win32).  Since it uses
the same back-end for all output, copying across formats is WYSIWYG. Files are
created without the dependence on X11 or other external programs. This device
supports alpha channel (semi-transparent drawing) and resulting images can
contain transparent and semi-transparent regions. It is ideal for use in server
environments (file output) and as a replacement for other devices that don't
have Cairo's capabilities such as alpha support or anti-aliasing. Backends are
modular such that any subset of backends is supported.

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
