# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/juju/ratelimit
%global goipath         github.com/juju/ratelimit
Version:                1.0.1

%gometa

%global common_description %{expand:
The ratelimit package provides an efficient token bucket implementation.}

%global golicenses      LICENSE
%global godocs          README.md

%global gosupfiles      glide.lock glide.yaml

Name:           %{goname}
Release:        %autorelease
Summary:        Efficient token-bucket-based rate limiter package

# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

%if %{with check}
# Tests
BuildRequires:  golang(gopkg.in/check.v1)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
cp %{S:1} %{S:2} .

%install
%gopkginstall

# Remove in F33
# Remove erroneous glide.lock folder
%pretrans devel -p <lua>
path = "%{gopath}/src/%{goipath}/glide.lock"
st = posix.stat(path)
if st and st.type == "directory" then
  os.remove(path)
end

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
