%define upstream_name Data-Dump-Streamer
%define upstream_version 2.32

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Accurately serialize a data structure as Perl code
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(B::Deparse)
BuildRequires:	perl(B::Utils)
BuildRequires:	perl(PadWalker)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Text::Abbrev)
BuildRequires:	perl(Text::Balanced)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl-devel
Requires:	perl(B::Utils)
Provides:	perl(Data::Dump::Streamer::_::Printers)

%description
Given a list of scalars or reference variables, writes out their contents in
perl syntax. The references can also be objects. The contents of each variable
is output using the least number of Perl statements as convenient, usually only
one. Self-referential structures, closures, and objects are output correctly.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
yes | perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorarch}/Data
%{perl_vendorarch}/DDS.pm
%{perl_vendorarch}/auto/Data


%changelog
* Sun Feb 12 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.320.0-1
+ Revision: 773658
- clean out spec
- new version
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 2.220.0-3
+ Revision: 681460
- add br
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2.220.0-2mdv2011.0
+ Revision: 555748
- rebuild for perl 5.12

* Thu Jul 15 2010 Jérôme Quelin <jquelin@mandriva.org> 2.220.0-1mdv2011.0
+ Revision: 553582
- update to 2.22

* Tue Apr 06 2010 Jérôme Quelin <jquelin@mandriva.org> 2.130.0-1mdv2010.1
+ Revision: 532141
- update to 2.13

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 2.90.0-1mdv2010.0
+ Revision: 401670
- rebuild using %%perl_convert_version
- fixed license field

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 2.09-2mdv2010.0
+ Revision: 374672
- update to 2.09 (for real this time)

* Fri May 01 2009 Jérôme Quelin <jquelin@mandriva.org> 2.09-1mdv2010.0
+ Revision: 369679
- update to new version 2.09

* Fri Jan 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.08_40-2mdv2009.1
+ Revision: 327396
- fix description and summary
- fix dependencies

* Thu Dec 04 2008 Jérôme Quelin <jquelin@mandriva.org> 2.08_40-1mdv2009.1
+ Revision: 309953
- all tests but one successful, shipping module
- adding missing build prereq
- force a provide, badly added by dependency lookup
  this way, the package will require something that it is providing, and
  thus the package will be installable
- import perl-Data-Dump-Streamer


* Wed Dec 03 2008 cpan2dist 2.08-40-1mdv
- initial mdv release, generated with cpan2dist

