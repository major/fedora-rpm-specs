%global octpkg jsonlab

Name:           octave-%{octpkg}
Version:        2.9.8
Release:        %autorelease
Summary:        A JSON/UBJSON/MessagePack encoder/decoder for MATLAB/Octave

%global forgeurl https://github.com/fangq/jsonlab
%forgemeta

License:        GPL-3.0-or-later OR BSD-3-Clause
URL:            http://openjdata.org/jsonlab
Source:         %forgesource
BuildArch:      noarch
BuildRequires:  octave-devel

Requires:       octave octave-zmat
Requires(post): octave
Requires(postun): octave

%description
JSONLab is a free and open-source implementation of a JSON/UBJSON/MessagePack 
encoder and a decoder in the native MATLAB language. It can be used to convert 
a MATLAB data structure (array, struct, cell, struct array and cell array) into
JSON/UBJSON formatted string, or decode a JSON/UBJSON/MessagePack file into 
MATLAB data. JSONLab supports both MATLAB and GNU Octave (a free MATLAB clone).
JSONLab is now the official reference implementation for the JData Specification 
(Draft 3) - the foundation of the OpenJData Project (http://openjdata.org).

%prep
%forgeautosetup

cp LICENSE_GPLv3.txt COPYING

mkdir -p inst/
rm Contents.m
mv *.m inst/

%build
%octave_pkg_build

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%license LICENSE_GPLv3.txt LICENSE_BSD.txt
%doc README.rst AUTHORS.txt ChangeLog.txt 
%doc examples
%doc test
%dir %{octpkgdir}
%{octpkgdir}/*.m
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo

%changelog
%autochangelog
