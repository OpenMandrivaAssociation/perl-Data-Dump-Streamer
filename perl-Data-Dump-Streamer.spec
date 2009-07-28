%define upstream_name    Data-Dump-Streamer
%define upstream_version 2.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Accurately serialize a data structure as Perl code
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(B::Deparse)
BuildRequires: perl(B::Utils)
BuildRequires: perl(PadWalker)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Abbrev)
BuildRequires: perl(Text::Balanced)
BuildRequires: perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}
Requires:      perl(B::Utils)
Provides:      perl(Data::Dump::Streamer::_::Printers)

%description
Given a list of scalars or reference variables, writes out their contents in
perl syntax. The references can also be objects. The contents of each variable
is output using the least number of Perl statements as convenient, usually only
one. Self-referential structures, closures, and objects are output correctly.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
echo yes | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorarch/Data
%perl_vendorarch/DDS.pm
%perl_vendorarch/auto/Data
