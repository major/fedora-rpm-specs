# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/streadway/amqp
%global goipath         github.com/streadway/amqp
Version:                1.0.0

%gometa

%global common_description %{expand:
Package Amqp is an AMQP 0.9.1 client with RabbitMQ extensions.}

%global golicenses      LICENSE
%global godocs          _examples CONTRIBUTING.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Go client for AMQP 0.9.1

# Upstream license specification: BSD-2-Clause
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
# Use outsdated insecure algorithm SHA1-RSA
for test in "TestTLSHandshake" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
# Fail on aarch64, upstream dead
%ifarch aarch64
rm -rvf client_test.go tls_test.go
%endif
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog